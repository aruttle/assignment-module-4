document.addEventListener('DOMContentLoaded', () => {
  const accommodationsDataElement = document.getElementById('accommodations-data');
  const bookedRangesElement = document.getElementById('booked-ranges-data');
  const accommodationTypeSelect = document.getElementById('accommodation_type');
  const accommodationSelect = document.getElementById('accommodation');

  const accommodations = accommodationsDataElement
    ? JSON.parse(accommodationsDataElement.textContent)
    : [];

  const bookedRanges = bookedRangesElement
    ? JSON.parse(bookedRangesElement.textContent)
    : [];

  // Populate accommodations when a type is selected
  function populateAccommodations(typeId) {
    accommodationSelect.innerHTML = '<option value="" disabled selected>Select accommodation</option>';
    accommodations
      .filter(acc => acc.type_id == typeId)
      .forEach(acc => {
        const option = document.createElement('option');
        option.value = acc.id;
        option.textContent = acc.name;
        accommodationSelect.appendChild(option);
      });
  }

  accommodationTypeSelect.addEventListener('change', function () {
    const selectedTypeId = this.value;
    populateAccommodations(selectedTypeId);
  });

  if (accommodationTypeSelect.value) {
    populateAccommodations(accommodationTypeSelect.value);
  }

  // Setup flatpickr
  const flatpickrConfig = {
    mode: 'range',
    dateFormat: 'Y-m-d',
    disable: bookedRanges.map(range => ({
      from: range.start,
      to: range.end
    }))
  };

  if (document.querySelector('#start_date')) {
    flatpickr('#start_date', flatpickrConfig);
  }
  if (document.querySelector('#end_date')) {
    flatpickr('#end_date', flatpickrConfig);
  }
});
