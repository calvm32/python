'''
Module for "Television" class.
'''
class Television:

    '''
    Class to represent television details.
    Initial values specified for min/max volume and min/max channel.
    '''

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        '''
        Television constructor to initialize a television object.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Toggles between television on and off.
        '''
        self.__status = not self.__status
    
    def mute(self) -> None:
        '''
        When power is on, toggles between television muted and not.
        '''
        if self.__status == True:
            self.__muted = not self.__muted
    
    def channel_up(self) -> None:
        '''
        When power is on, increases channel by 1.
        Goes from max channel value down to min channel value.
        '''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    def channel_down(self) -> None:
        '''
        When power is on, decreases channel by 1.
        Goes from min channel value up to max channel value.
        '''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self) -> None:
        '''
        When power is on, sets television to unmute and increases volume by 1.
        Will not increase past max volume.
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        '''
        When power is on, sets television to unmute and decreases volume by 1.
        Will not decrease past min volume.
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Displays power, channel, and volume in the format 
        'Power = [power], Channel = [channel], Volume = volume'.
        Note when telivision is muted, displayed volume is 0 regardless of volume value.
        '''
        displayVolume = self.__volume
        if self.__muted == True:
            displayVolume = 0
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {displayVolume}'