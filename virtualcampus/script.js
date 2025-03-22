let map, panorama;

function initMap() {
    const iitDelhi = { lat: 28.5450, lng: 77.1926 }; // IIT Delhi Main Gate

    // Initialize Street View
    panorama = new google.maps.StreetViewPanorama(
        document.getElementById("street-view"),
        {
            position: iitDelhi,
            pov: { heading: 165, pitch: 0 },
            zoom: 1
        }
    );

    // Initialize Map
    map = new google.maps.Map(document.getElementById("campus-map"), {
        center: iitDelhi,
        zoom: 16,
        streetViewControl: false
    });

    // Add Marker
    new google.maps.Marker({
        position: iitDelhi,
        map: map,
        title: "IIT Delhi Main Campus"
    });

    // Set Street View
    map.setStreetView(panorama);
}

// Function to change location
function changeLocation(lat, lng) {
    const newLocation = { lat: lat, lng: lng };
    panorama.setPosition(newLocation);
    map.setCenter(newLocation);
}
