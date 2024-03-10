from typing import Any

import streamlit as st
class Fighter:
    """
    A class for a fighter

    Attributes:
        Rarity: The fighters rarity
        Name: The fighters name
        Color: The fighters color
        Tags: The fighters tags
        Z-Tags: The tags the fighter supports with their z-ability
        IMG: The fighters image
    """

    rarity: str
    name: str
    color: str
    tags: list
    ztags: list
    img: Any
    epi: str
    dbl: str

    def __init__(self, rarity: str, name: str, color: str, tags: list,
                 ztags: list, img: Any, epi: str, dbl: str):
        self.rarity = rarity
        self.name = name
        self.color = color
        self.tags = tags.copy()
        self.ztags = ztags.copy()
        self.img = img
        self.epi = epi
        self.dbl = dbl


    def __str__(self):
        hold = self.name.split(".")
        return hold[0] + " (" + self.dbl + ")"


    def __eq__(self, other):
        return str(self) == str(other)
