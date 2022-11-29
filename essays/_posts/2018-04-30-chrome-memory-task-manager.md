---
title: Exploring the Memory Tab in Chrome Task Manager
description: Performance leaks in the Chrome Browser are common and hard to detect. This is simple first-level diagnostic to track down memory leaks and problems.
date: 2018-04-30
layout: essay
tags:
  - web-and-performance
---

# Getting to the Task Manager

- Shortcut: Shift + Esc, **OR**
- Chrome -> Settings -> More Tools -> Task Manager

# Understanding Memory Usage Columns in Task Manager

## Memory Footprint

The memory footprint represents memory reserved entirely for that process. It is the same value as that in the **Commit Size** column in Windows Task Manager. _The Commit column shows the amount of virtual memory in kilobytes that the operating system has reserved for a process. This number includes the amount of physical memory that is in use as well as any pages that have been saved in the page file._

- # Memory

  Memory is the same value as that in the **Memory (Private Working Set)** column in Windows Task Manager. Private Working Set of a process refers to the amount of memory that is allocated to the process, is not shareable. In Chrome context, it refers to the native memory, which is used to store DOM nodes. A constantly increasing value for this indicates creation of additional DOM noes.

- # GPU Memory

  It represents the amount of GPU memory being used by the page. The GPU process is a process used only when Chrome is displaying GPU-accelerated content. Chrome uses GPU to accelerate web-page rendering, typical HTML, CSS, WebGL, etc.

- # Javascript Memory
  The JavaScript Memory column represents the memory reserved for the JS VM heap. The number in parenthese is represents how much memory the reachable objects on your page are using. So, if the value is x ( y ) imples that 'y' is the active memory and (x-y) is memory is unreachable and will be garbage collected. If 'x' is increasing, it might signify a memory leak since either new objects are being created, or the existing objects are growing.

# References:

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/memory-problems/#monitor_memory_use_in_realtime_with_the_chrome_task_manager)
- [Stackoverflow](https://stackoverflow.com/questions/14167013/javascript-memory-and-leak-problems)
- [investigate-memory-usage-with-windows-7-resource-monitor/](https://www.techrepublic.com/blog/windows-and-office/investigate-memory-usage-with-windows-7-resource-monitor/)
