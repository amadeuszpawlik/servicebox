from django.db import models

from users.models import User

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               related_name='events',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)

    def get_payload(self):
        try:
            return self.comment
        except:
            pass

        try:
            return self.assignment
        except:
            pass

        return self

class Comment(Event):
    message = models.CharField(max_length=1000, blank=False)

    def get_type(self):
        return "comment"

    def __str__(self):
        return str(self.author.get_username()) + " commented " + str(self.created)


class Assignment(Event):
    assigned = models.BooleanField(default=False)
    assignee = models.ForeignKey(User,
                                 related_name='events_assignments',
                                 null=True,
                                 blank=False,
                                 on_delete=models.SET_NULL)

    def get_type(self):
        return "assignment"

    def __str__(self):
        if self.assigned:
            return self.author.get_username() + " assigned " + self.assignee.get_username()
        else:
            return self.author.get_username() + " unassigned " + self.assignee.get_username()
