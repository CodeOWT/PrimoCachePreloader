# PrimoCache Multithreaded Preloader Script

This script, inspired by RobF's post on the [Romex Software Forum](https://forum.romexsoftware.com/en-us/viewtopic.php?p=11033#p11033), is designed to facilitate the preloading of files into PrimoCache's L2 cache. PrimoCache typically populates its L2 cache incrementally over time, which can take days or weeks, and it might not prioritize the files you need the most. This script preloads the files into PrimoCache by systematically reading files from a specified directory, thereby ensuring their addition to PrimoCache's cache in a more immediate and targeted manner.

**The script only reads files and does not perform any modifications or deletions.**

## Requirements

- Python 3.x

## Usage

**Command Line Arguments:**

1. **Starting Directory**: The path to files you wish to read and preload into PrimoCache.
2. **File Pattern**: Specifies the file pattern to be read. Use `*.*` to include all files.

**Example Command:**

```bash
C:\> python primocache_preloader.py C:\Path\to\Folder *.*
```

This command will read all files in `C:\Path\to\Folder`, which should trigger PrimoCache to write the file to its L2 cache.

## Configuration

**Adjusting Thread Count:**

The script uses multithreading to enhance performance by concurrently reading multiple files. To adjust the number of threads according to your system's capabilities or specific needs, modify the `max_threads` variable in the script:

```python
max_threads = 4 # Default value
```

Change `4` to your desired number of concurrent threads.