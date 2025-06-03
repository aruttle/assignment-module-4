document.addEventListener('DOMContentLoaded', () => {
  const accommodations = JSON.parse(document.getElementById('accommodations-data').textContent);
  const bookedRangesByAccommodation = JSON.parse(document.getElementById('booked-ranges-data').textContent);

  const accommodationTypeSelect = document.getElementById('accommodation_type');
  const accommodationSelect = document.getElementById('accommodation');

  let startPicker = null;
  let endPicker = null;

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
    // Reset date inputs and destroy pickers when accommodation list changes
    resetDatePickers();
  }

  function resetDatePickers() {
    if (startPicker) {
      startPicker.destroy();
      startPicker = null;
    }
    if (endPicker) {
      endPicker.destroy();
      endPicker = null;
    }
    document.getElementById('start_date').value = '';
    document.getElementById('end_date').value = '';
  }

  function updateFlatpickr(accommodationId) {
    const ranges = bookedRangesByAccommodation[accommodationId] || [];

    const disableRanges = ranges.map(range => ({
      from: range.start,
      to: range.end
    }));

    // Destroy previous pickers before re-creating
    if (startPicker) startPicker.destroy();
    if (endPicker) endPicker.destroy();

    startPicker = flatpickr("#start_date", {
      dateFormat: 'Y-m-d',
      disable: disableRanges,
      onChange(selectedDates) {
        if (selectedDates.length > 0) {
          // Set minDate for endPicker based on start date selection
          const minEndDate = selectedDates[0];
          endPicker.set('minDate', minEndDate);
          // Optionally clear end date if it's before start date
          if (endPicker.selectedDates.length > 0 && endPicker.selectedDates[0] < minEndDate) {
            endPicker.clear();
          }
        }
      }
    });

    endPicker = flatpickr("#end_date", {
      dateFormat: 'Y-m-d',
      disable: disableRanges,
      // Initially, disable dates before start date if selected
      minDate: startPicker.selectedDates.length > 0 ? startPicker.selectedDates[0] : null,
    });
  }

  accommodationTypeSelect.addEventListener('change', function () {
    const selectedTypeId = this.value;
    populateAccommodations(selectedTypeId);
  });

  accommodationSelect.addEventListener('change', function () {
    const selectedAccommodationId = this.value;
    if (selectedAccommodationId) {
      updateFlatpickr(selectedAccommodationId);
    } else {
      resetDatePickers();
    }
  });

  // On page load, if accommodation type is already selected, populate accommodations
  if (accommodationTypeSelect.value) {
    populateAccommodations(accommodationTypeSelect.value);
  }
});
