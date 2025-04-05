class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Participant: {self.name}, Email: {self.email}"


class Activity:
    def __init__(self, name, description, start_time, end_time):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (f"Activity: {self.name}, Description: {self.description}, "
                f"Time: {self.start_time} - {self.end_time}")


class Organizer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(festself):
        return f"Organizer: {self.name}, Contact: {self.contact}"


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        self.activities = []
        self.organizers = []

    def add_participant(self, participant):
        self.participants.append(participant)
        print(f"Participant {participant.name} has been registered.")

    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"Activity '{activity.name}' has been added to the schedule.")

    def add_organizer(self, organizer):
        self.organizers.append(organizer)
        print(f"Organizer {organizer.name} has been assigned.")

    def display_schedule(self):
        print(f"\nSchedule for Eventorganizersent: {self.name}")
        for participant in self.participants:
            print(participant)

    def display_organizers(self):
        print(f"\nOrganizers for Event: {self.name}")
        for organizer in self.organizers:
            print(organizer)


# Create an event
fest = Event("TechFest 2024", "2024-12-15")

# Add organizers
organizer1 = Organizer("Alice", "alice@example.com")
organizer2 = Organizer("Bob", "bob@example.com")
fest.add_organizer(organizer1)
fest.add_organizer(organizer2)

# Add participants
participant1 = Participant("Charlie", "charlie@example.com")
participant2 = Participant("Diana", "diana@example.com")
fest.add_participant(participant1)
fest.add_participant(participant2)

# Add activities
activity1 = Activity("Coding Contest", "Solve programming challenges", "10:00 AM", "12:00 PM")
activity2 = ActiviOrganizertails
fest.display_schedule()
fest.display_participants()
fest.display_organizers()