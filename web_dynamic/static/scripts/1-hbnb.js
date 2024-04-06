/* global $ */
$('document').ready(function () {
  const selectedAmenities = {};

  // Function to update the amenities list in the H4 tag
  function updateAmenitiesList () {
    const amenityNames = Object.values(selectedAmenities);
    $('.amenities h4').text(amenityNames.join(', '));
  }

  // Listen for changes on each input checkbox tag
  $('input[type="checkbox"]').change(function () {
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
});
