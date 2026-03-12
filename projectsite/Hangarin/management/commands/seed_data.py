from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from Hangarin.models import Task, Note, SubTask, Category, Priority, StatusChoices


class Command(BaseCommand):
    help = "Seed fake data for Task, Note, and SubTask"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR("Add categories and priorities first."))
            return

        for _ in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=[
                    StatusChoices.PENDING,
                    StatusChoices.IN_PROGRESS,
                    StatusChoices.COMPLETED,
                ]),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )

            for _ in range(random.randint(1, 3)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

            for _ in range(random.randint(1, 5)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=[
                        StatusChoices.PENDING,
                        StatusChoices.IN_PROGRESS,
                        StatusChoices.COMPLETED,
                    ]),
                )

        self.stdout.write(self.style.SUCCESS("Fake data created successfully."))