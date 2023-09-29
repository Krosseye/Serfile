"""
Dictionary mapping file extensions to emoji icons.

Keys are file extensions (e.g., ".jpg", ".mp3"),
and values are emoji icons (e.g., "🖼️", "🎵").
"""

from typing import Dict

ICON_MAP: Dict[str, str] = {
    # Image Formats
    ".jpg": "🖼️",  # JPEG image
    ".jpeg": "🖼️",  # JPEG image
    ".png": "🖼️",  # PNG image
    ".gif": "🖼️",  # GIF image
    ".bmp": "🖼️",  # BMP image
    ".svg": "🖼️",  # SVG image
    ".webp": "🖼️",  # WebP image
    ".ico": "🖼️",  # Icon file
    ".tif": "🖼️",  # TIFF image
    ".tiff": "🖼️",  # TIFF image
    ".jp2": "🖼️",  # JPEG 2000 image
    ".jxr": "🖼️",  # JPEG XR image
    # Audio Formats
    ".mp3": "🎵",  # MP3 audio
    ".wav": "🎵",  # WAV audio
    ".ogg": "🎵",  # OGG audio
    ".flac": "🎵",  # FLAC audio
    ".aac": "🎵",  # AAC audio
    ".wma": "🎵",  # WMA audio
    ".m4a": "🎵",  # M4A audio
    # Video Formats
    ".mp4": "📹",  # MP4 video
    ".avi": "📹",  # AVI video
    ".mkv": "📹",  # MKV video
    ".mov": "📹",  # QuickTime video
    ".wmv": "📹",  # WMV video
    ".flv": "📹",  # Flash video
    ".webm": "📹",  # WebM video
    # Document Formats
    ".txt": "📝",  # Text file
    ".rtf": "📝",  # Rich Text Format
    ".md": "📝",  # Markdown file
    ".pdf": "📄",  # PDF document
    ".doc": "📑",  # DOC document
    ".docx": "📑",  # DOCX document
    ".odt": "📑",  # OpenDocument Text
    ".odp": "📊",  # OpenDocument Presentation
    ".ods": "📈",  # OpenDocument Spreadsheet
    ".ppt": "📊",  # PowerPoint presentation
    ".pptx": "📊",  # PowerPoint presentation
    ".xls": "📈",  # Excel spreadsheet
    ".xlsx": "📈",  # Excel spreadsheet
    # Data Formats
    ".csv": "📊",  # CSV file
    ".json": "📊",  # JSON file
    ".xml": "📜",  # XML file
    # Archive Formats
    ".zip": "🗃️",  # Zip archive
    ".rar": "🗃️",  # RAR archive
    ".7z": "🗃️",  # 7-Zip archive
    ".tar": "🗃️",  # Tarball archive
    ".gz": "🗃️",  # Gzip archive
    ".bz2": "🗃️",  # Bzip2 archive
    ".xz": "🗃️",  # XZ archive
    # Executable Formats
    ".exe": "💿",  # Executable file
    ".msi": "💿",  # Windows Installer package
    ".bin": "💿",  # Binary executable
    ".out": "💿",  # Compiled output
    ".run": "💿",  # Runnable file
    ".app": "📱",  # Application file
    ".apk": "📱",  # Android package
    ".ipa": "📱",  # iOS app
    ".jar": "📦",  # Java Archive
    ".deb": "📦",  # Debian package
    ".rpm": "📦",  # RPM package
    ".dll": "💾",  # DLL file
    # Programming & Script Formats
    ".bat": "📜",  # Batch script
    ".cmd": "📜",  # Command script
    ".sh": "📜",  # Shell script
    ".command": "📜",  # Command script
    ".py": "🐍",  # Python script
    ".cpp": "💻",  # C++ source code
    ".java": "☕",  # Java source code
    ".js": "📜",  # JavaScript source code
    ".html": "📄",  # HTML file
    ".css": "🎨",  # CSS file
    ".rb": "💎",  # Ruby script
    ".php": "🐘",  # PHP script
    ".swift": "🍏",  # Swift script
    ".pl": "🐪",  # Perl script
    ".lua": "🌙",  # Lua script
    ".ps1": "📜",  # PowerShell script
    ".vb": "⌨️",  # Visual Basic script
    ".ts": "📜",  # TypeScript file
    ".kotlin": "☕",  # Kotlin Source Code
    ".go": "🐹",  # Go Source Code
    ".rs": "🦀",  # Rust Source Code
    ".cs": "#️⃣",  # C# Source Code
    ".c": "🅒",  # C Source Code
    # Disk Image Formats
    ".dmg": "💾",  # macOS disk image
    ".iso": "💿",  # ISO disk image
    ".img": "💿",  # Generic disk image
    ".vhd": "🗃️",  # Virtual Hard Disk (VHD)
    ".vhdx": "🗃️",  # Virtual Hard Disk (VHDX)
    ".vmdk": "🗃️",  # Virtual Machine Disk (VMDK)
    ".cue": "📀",  # CUE file
    # Vector & Graphic Design Formats
    ".ai": "🖼️",  # Adobe Illustrator
    ".eps": "🖼️",  # Encapsulated PostScript
    ".psd": "🖼️",  # Adobe Photoshop
    ".xcf": "🖼️",  # GIMP image
    # 3D & Design Formats
    ".obj": "🏗️",  # Waveform Object 3D file
    ".stl": "🏗️",  # Stereolithography 3D model
    ".3ds": "🏗️",  # 3DS Max 3D model
    ".fbx": "🏗️",  # Autodesk FBX 3D model
    ".blend": "🏗️",  # Blender 3D model
    ".blend1": "🏗️",  # Blender 3D model
    ".c4d": "🏗️",  # Cinema 4D File Format
    ".max": "🏗️",  # 3ds Max Scene File Format
    # Font Formats
    ".ttf": "🔡",  # TrueType font
    ".otf": "🔡",  # OpenType font
    ".woff": "🔡",  # WebOpenFontFormat font
    ".woff2": "🔡",  # WebOpenFontFormat font
    # Miscellaneous Formats
    ".torrent": "🔗",  # Torrent file
    ".cfg": "⚙️",  # Configuration file
    ".config": "⚙️",  # Configuration file
    ".ini": "⚙️",  # INI configuration file
    ".url": "🔗",  # URL shortcut
    ".lnk": "🔗",  # Windows shortcut
}
