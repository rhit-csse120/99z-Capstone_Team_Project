"""
The  Controller  file for the Model-View-Controller architecture for our game.
Its   get_and_handle_events   method is called repeatedly by the main game loop.
At each call, it gets and handles whatever event(s) occurred,
typically by asking the various objects of the Game to do things.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

import pygame
import sys
from Game import Game


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """
        Called by the main game loop.
        Gets events, then asks the Game's appropriate objects to handle them.
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()

        # TODO: Use code like the following, but for YOUR Game object.
        #     if pressed_keys[pygame.K_LEFT]:
        #         self.game.fighter.move_left()
        #     if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
        #         self.game.fighter.fire()

    @staticmethod
    def exit_if_time_to_quit(events):
        """ Exits the program if the QUIT event occurs. """
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        """ Returns True if the given key was pressed on this cycle. """
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
