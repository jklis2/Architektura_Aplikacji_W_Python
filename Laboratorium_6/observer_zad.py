# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:02:55 2024

@author: Przemysław
"""

from abc import ABC, abstractmethod

class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        """Adds an observer to the list of observers.

        Args:
            observer (Observer): The object that will observe changes.
        """
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Removes an observer from the list of observers.

        Args:
            observer (Observer): The object that will stop observing changes.
        """
        self._observers.remove(observer)

    def notify_observers(self, message):
        """Notifies all observers with a given message.

        Args:
            message (str): The message to send to observers.
        """
        for observer in self._observers:
            observer.update(self, message)

class Observer(ABC):
    @abstractmethod
    def update(self, observable, message):
        """Abstract method to be implemented by concrete observers to handle updates.

        Args:
            observable (Observable): The observable object that is notifying observers.
            message (str): The message sent by the observable.
        """
        pass

class Twitter(Observable, Observer):
    def __init__(self, name):
        Observable.__init__(self)
        self.name = name
        self.following = []

    def follow(self, other):
        """Follows another Twitter user, adding this user as an observer.

        Args:
            other (Twitter): The Twitter user to follow.

        Returns:
            self: Returns the current instance for chaining.
        """
        if other not in self.following:
            self.following.append(other)
            other.add_observer(self)
        return self

    def tweet(self, message):
        """Sends a tweet and notifies all followers.

        Args:
            message (str): The content of the tweet.
        """
        self.notify_observers(message)

    def update(self, observable, message):
        """Receives a tweet from an observable Twitter user.

        Args:
            observable (Twitter): The Twitter user sending the tweet.
            message (str): The content of the tweet.
        """
        print(f'{self.name} received a tweet from {observable.name}: {message}')

if __name__ == "__main__":
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')
    
    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)
    
    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')
