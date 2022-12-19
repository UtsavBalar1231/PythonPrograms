# /usr/bin/env python3
import threading
import random
import time


class Philosopher(threading.Thread):
    """
    Philosopher is a subclass of Thread. It has a run method that is called when the thread starts.
    The run method calls dine, which in turn calls dining.
    dining is where the philosopher actually eats.
    The dine method first acquires the chopsticks, then calls dining.
    When dining is done, the chopsticks are released.
    The dine method also checks to see if the philosopher is still hungry.
    If not, the thread terminates.
    """
    running = True

    def __init__(self, _name, leftChopstick, rightChopstick):
        """
        The Philosopher class is initialized with a name and two chopsticks.
        """
        threading.Thread.__init__(self)
        self.name = _name
        self.leftChopstick = leftChopstick
        self.rightChopstick = rightChopstick

    def run(self):
        """
        The run method calls dine, which in turn calls dining.
        """
        while(self.running):
            print('%s is hungry and thinking. ' % self.name)
            self.dine()

    def dine(self):
        """
        The dine method first acquires the chopsticks, then calls dining.
        When dining is done, the chopsticks are released.
        """
        chopstick1, chopstick2 = self.leftChopstick, self.rightChopstick

        while self.running:
            # The philosopher first tries to acquire the chopstick on the left.
            chopstick1.acquire(True)
            # Try to acquire the chopstick on the right.
            locked = chopstick2.acquire(False)
            if locked:
                print()
                print('%s acquires both chopsticks. ' % self.name)
                break

            # release the chopstick on the left and try again
            print('%s unable to acquire both chopsticks. ' % self.name)
            chopstick1.release()
            chopstick1, chopstick2 = chopstick2, chopstick1
        else:
            return

        self.dining()

        # release the chopsticks
        print('%s releases both chopsticks. ' % self.name)
        chopstick2.release()
        chopstick1.release()

    def dining(self):
        print('%s starts eating. ' % self.name)
        self.running = False


def DiningPhilosophers():
    chopsticks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Daemon', 'Rhaenrya', 'Viserys', 'Alicent', 'Aemon')

    # Create five philosophers and start them eating
    philosophers = [Philosopher(philosopherNames[i], chopsticks[i % 5], chopsticks[(i+1) % 5])
                    for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(5)
    Philosopher.running = False
    print("Now we're finished.")


if __name__ == "__main__":
    DiningPhilosophers()
