/* global $ */
$('document').ready(function () {
  const selectedAmenities = {};
  const selectedStates = {};

  // Function to update the amenities list in the H4 tag
  function updateAmenitiesList () {
    const amenityNames = Object.values(selectedAmenities);
    $('.amenities h4').text(amenityNames.join(', '));
  }

  // New function to update the states list in the H4 tag
  function updateStatesList () {
    const stateNames = Object.values(selectedStates);
    $('.locations h4').text(stateNames.join(', '));
  }

  // Listen for changes on each input checkbox tag
  $('.amenities input[type="checkbox"]').change(function () {
    const amenityId = $(this).data('id');
    const amenityName = $(this).data('name');

    if (this.checked) {
      selectedAmenities[amenityId] = amenityName;
    } else {
      delete selectedAmenities[amenityId];
    }

    const amenityNames = Object.values(selectedAmenities);
    $('.amenities h4').text(amenityNames.join(', '));

    updateAmenitiesList();
  });

  // New function to listen for changes on each input checkbox tag
  $('.locations input[type="checkbox"]').change(function () {
    const stateId = $(this).data('id');
    const stateName = $(this).data('name');

    if (this.checked) {
      selectedStates[stateId] = stateName;
    } else {
      delete selectedStates[stateId];
    }

    const stateNames = Object.values(selectedStates);
    $('.locations h4').text(stateNames.join(', '));

    updateStatesList();
  });

  $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });

  // Fetch places and display them on the page
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/places_search/',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: function (data) {
      $('SECTION.places').append(data.map(place => {
        return `<ARTICLE>
                    <DIV class="place_head">
                        <H2>${place.name}</H2>
                        <DIV class="price_by_night">&#36;${place.price_by_night}</DIV>
                    </DIV>
                    <DIV class="information">
                        <DIV class="max_guest">${place.max_guest} Guests</DIV>
                        <DIV class="number_rooms">${place.number_rooms} Bedroom</DIV>
                        <DIV class="number_bathrooms">${place.number_bathrooms} Bathroom</DIV>
                    </DIV>
                    <DIV class="description">${place.description}</DIV>
                </ARTICLE>`;
      }));
    }
  });
  $('.filters > button').click(function () {
    $('.places > article').remove();
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/places_search',
      data: JSON.stringify({
        amenities: Object.keys(selectedAmenities),
        states: Object.keys(selectedStates)
      }),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
        $('SECTION.places').append(data.map(place => {
          return `<ARTICLE>
                    <DIV class="place_head">
                        <H2>${place.name}</H2>
                        <DIV class="price_by_night">&#36;${place.price_by_night}</DIV>
                    </DIV>
                    <DIV class="information">
                        <DIV class="max_guest">${place.max_guest} Guests</DIV>
                        <DIV class="number_rooms">${place.number_rooms} Bedroom</DIV>
                        <DIV class="number_bathrooms">${place.number_bathrooms} Bathroom</DIV>
                    </DIV>
                    <DIV class="description">${place.description}</DIV>
                </ARTICLE>`;
        }));
      }
    });
  });
});
