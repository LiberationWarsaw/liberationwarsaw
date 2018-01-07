function filterAllEvents() {
  var unselected_events = document.querySelectorAll('.event-page-item');

  for (i = 0; i < unselected_events.length; i++) {
    unselected_events[i].classList.add('inactive');
  }
}

function clearFilters() {
  var unselected_events = document.querySelectorAll('.event-page-item');

  for (i = 0; i < unselected_events.length; i++) {
    unselected_events[i].classList.remove('inactive');
  }

  var buttons = document.querySelectorAll('.filter.button');

  for (i = 0; i < buttons.length; i++) {
    buttons[i].classList.remove('active');
  }
}

function filterEvents(query, button) {
  var selected_events = document.querySelectorAll(query);

  function toggleEvents() {
    for (i = 0; i < selected_events.length; i++) {
      selected_events[i].classList.toggle('inactive');
    }
  }

  function toggleButton() {
    console.log(button);
    button.classList.toggle('active');
    console.log('changed');
  }

// If button is inactive:
  if (button.classList.contains('active') == true) {
    clearFilters();
    console.log('True');
// If button is already active:
  } else {
    clearFilters();
    filterAllEvents();
    toggleEvents();
    toggleButton();
    console.log('False');
  }
}
