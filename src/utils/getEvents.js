
import ical from 'ical';

export async function getUpcomingEvents() {
  // REPLACE THIS with your Club's Public Calendar Secret Address (ICAL format)
  // You get this from GCal Settings > Integrate Calendar > Secret address in iCal format
  const CALENDAR_URL = 'https://calendar.google.com/calendar/ical/67aefd4dd7621c22897c0a8fdd47453ee92c5d6d55de02e1b1e5465cfa4a7027%40group.calendar.google.com/public/basic.ics';

  const response = await fetch(CALENDAR_URL);
  const data = await response.text();
  const events = ical.parseICS(data);

  // Convert object to array and filter
  const upcoming = Object.values(events)
    .filter(event => event.type === 'VEVENT')
    .filter(event => new Date(event.start) >= new Date()) // Only future events
    .sort((a, b) => new Date(a.start) - new Date(b.start)) // Sort by date
    .slice(0, 5); // Limit to next 5 events

  // Format for your Astro Component
  return upcoming.map(event => {
    const date = new Date(event.start);
    const month = date.toLocaleString('default', { month: 'short' }).toUpperCase();
    const day = date.getDate();
    
    // Format time (e.g., "9:00 AM - 4:00 PM")
    const timeOptions = { hour: 'numeric', minute: '2-digit' };
    const startTime = date.toLocaleTimeString('en-US', timeOptions);
    const endTime = new Date(event.end).toLocaleTimeString('en-US', timeOptions);

    return {
      day: day,
      month: month,
      title: event.summary,
      time: `${startTime} - ${endTime}`,
      location: event.location || "Club Flying Field",
      description: event.description || "No description provided.",
      linkText: "Add to Calendar",
      linkUrl: "#", // You could generate a gcal link here if you wanted
      color: "bg-primary" // Default color
    };
  });
}