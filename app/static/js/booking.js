document.addEventListener('DOMContentLoaded', () => {
  const accommodations = JSON.parse(document.getElementById('accommodations-data').textContent);
  const accommodationTypeSelect = document.getElementById('accommodation_type');
  const accommodationSelect = document.getElementById('accommodation');

  function populateAccommodations(typeId) {
    accommodationSelect.innerHTML = '<option value="" disabled selected>Select accommodation</option>';
    accommodations.forEach(acc => {
      if (acc.type_id == typeId) {
        const option = document.createElement('option');
        option.value = acc.id;
        option.textContent = acc.name;
        accommodationSelect.appendChild(option);
      }
    });
  }

  accommodationTypeSelect.addEventListener('change', function () {
    const selectedTypeId = this.value;
    populateAccommodations(selectedTypeId);
  });

  if (accommodationTypeSelect.value) {
    populateAccommodations(accommodationTypeSelect.value);
  }
});
