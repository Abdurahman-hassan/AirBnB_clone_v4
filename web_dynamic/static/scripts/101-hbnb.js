/* global $ */
$('document').ready(function () {
    let selectedAmenities = {};
    let selectedStates = {};
    let users = {};

    // Fetch users and store them in a dictionary
    $.get('http://0.0.0.0:5001/api/v1/users/', function (data) {
        for (let i = 0; i < data.length; i++) {
            users[data[i].id] = data[i].first_name + ' ' + data[i].last_name;
        }
    });

    // Fetch reviews and display them on the page
    function fetchAndDisplayReviews(placeId) {
        $.get(`http://0.0.0.0:5001/api/v1/places/${placeId}/reviews`, function (data) {
            const reviewList = $(`ARTICLE[data-id="${placeId}"] .reviews .review_list`);
            reviewList.empty();
            data.forEach(review => {
                reviewList.append(`
                <LI>
                    <H3>${users[review.user_id]} ${new Date(review.created_at).toLocaleDateString()}</H3>
                    <P>${review.text}</P>
                </LI>
            `);
            });
        });
    }
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
                return `<ARTICLE data-id="${place.id}">
                    <DIV class="place_head">
                        <H2>${place.name}</H2>
                        <DIV class="price_by_night">&#36;${place.price_by_night}</DIV>
                    </DIV>
                    <DIV class="information">
                        <DIV class="max_guest">${place.max_guest} Guests</DIV>
                        <DIV class="number_rooms">${place.number_rooms} Bedroom</DIV>
                        <DIV class="number_bathrooms">${place.number_bathrooms} Bathroom</DIV>
                    </DIV>
                    <DIV class="owner">${users[place.user_id]}</DIV>
                    <DIV class="description">${place.description}</DIV>
                    <DIV class="reviews">
                        <H2>Reviews <SPAN class="toggle_reviews" data-place-id="${place.id}">show</SPAN></H2>
                        <UL class="review_list">
                            <!-- Reviews will be added here by JavaScript -->
                        </UL>
                    </DIV>
                </ARTICLE>`;
            }));

            $('SECTION.places').on('click', '.toggle_reviews', function () {
                const placeId = $(this).data('place-id');
                const reviewList = $(`ARTICLE[data-id="${placeId}"] .reviews .review_list`);
                if ($(this).text() === 'show') {
                    fetchAndDisplayReviews(placeId);
                    $(this).text('hide');
                } else {
                    reviewList.empty();
                    $(this).text('show');
                }
            });
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
                    return `<ARTICLE data-id="${place.id}">
                <DIV class="place_head">
                    <H2>${place.name}</H2>
                    <DIV class="price_by_night">&#36;${place.price_by_night}</DIV>
                </DIV>
                <DIV class="information">
                    <DIV class="max_guest">${place.max_guest} Guests</DIV>
                    <DIV class="number_rooms">${place.number_rooms} Bedroom</DIV>
                    <DIV class="number_bathrooms">${place.number_bathrooms} Bathroom</DIV>
                </DIV>
                <DIV class="owner">${users[place.user_id]}</DIV>
                <DIV class="description">${place.description}</DIV>
                <DIV class="reviews">
                    <H2>Reviews <SPAN class="toggle_reviews" data-place-id="${place.id}">show</SPAN></H2>
                    <UL class="review_list">
                        <!-- Reviews will be added here by JavaScript -->
                    </UL>
                </DIV>
            </ARTICLE>`;
                }));
            }
        });
    });
});
