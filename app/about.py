"""This module contains information about the application."""

from typing import Dict, List

APP_VERSION: str = "0.11.7 (Alpha Pre-release)"

Asset = Dict[str, str]

licenses: Dict[str, List[Asset]] = {
    "assets": [
        {
            "name": "Noto Color Emoji",
            "version": "Unicode 15.0",
            "license": "SIL Open Font License, version 1.1",
        },
        {
            "name": "Inter Font",
            "version": "3.19",
            "license": "SIL Open Font License, version 1.1",
        },
        {"name": "Sortable", "version": "2.3.2", "license": "The Unlicense"},
        {
            "name": "Ace",
            "version": "1.5.0",
            "license": "Copyright (c) 2010, Ajax.org B.V. All rights reserved.",
        },
        {
            "name": "Fira Code",
            "version": "6.3",
            "license": "SIL Open Font License, version 1.1",
        },
        {
            "name": "Fluent UI System Icons",
            "version": "1.1.217",
            "license": "MIT License",
        },
    ]
}
