---
title: "Refactoring UI: Adam Wathan and Steve Schoger"
description: From the makers of TailwindCSS, this is only design guide a developer will ever need.
date: 2023-12-07
layout: post
---

PS: This is my stack of of notes from this awesome [resource](https://www.refactoringui.com/).

## Getting started

- Don't design too much, eliminate as much as possible. Design a little, reiterate.
- Build systems
- start with a feature, not a layout (break it down)
- DONT think about the shell
- app => collection of features
- start with a piece of functionality
- details come later - dont get stuck on making low-level decisions like typefaces, shadows and icons
- jason fried, basecamp => design on paper with a sharpie
- hold the color: DONOT introduce color; design in grayscale; cleaner + strong hierarchy
- don't overinvest: move fast, low fidelity; use only to make decisions; leave them behind once done
- don't over-design: dont design every single feature in the app before implementation; it's better not to. edge cases are hard.  you'll set yourself up for frustration
- work in cycles - design a simple version; leave it; iterate
- make a basic design, then make it real;
- iterate on the working design until there are no more problems to solve; design <> code; build the real thing so that your imagination doesn't need to do all the heavy lifting
- be a pessimist - do design for functionality you won't have
- when designing a new feature, expect it to be hard to build
- nice to have => design later
- choose a personality
- font choice
- elegant or classic => serif
- playful look => rounded sans serif
- plainer => neutral sans serif
- color
- blue is safe and familiar
- gold is expensive
- pink is fun
- color psychology
- border radius
- larger border radius => more playful
- no border radius => formal
- stick to one
- language
- use playful language with playful fonts
- decide on what you want; look at the competition but dont borrow too much
- limit your choices
- what are the components of a design system?
- wasteful options
- define systems in advance - pick shades ahead of time and pick from that
- pick from limited set of font sizes
- icon sizes
- fontsize, font weight, line height, color, margin, padding, width, height, box shadows, border radius, border width, opacity

## Hierarchy is everything

- not all element are equal
- strategies:
- size isn't everything
- use font-weight and font-color
- stick to 2-3 colors (dark color for primary, grey for secondary, lighter gray for tertiary)
- 2 font-weights: 400-500, 600-700
- stay away from < 400 (use a lighter color or font size instead)
- dont use grey text on colored backgrounds (how would i automate this; effect is reduced in contrast) make it closer to the background color to deemphasize; use the same hue and adjust saturation and lightness till it looks right
- de-emphasize instead of emphasizing
- labels are last resort; add label but treat it like supporting content
- for information dense pages, where user would be looking for labels  - like product specs, emphasize there
- separate visual hierarchy from document hierarchy
- use semantic markup; but dont style accordingly
- balance weight and contrast
- bold covers more surface area, hence looks emphasized
- surface area and hierarchy have a relationship
- use contrast to balance out over weighted icons
- semantics are secondary
- primary - high contrast backgrounds
- secondary - outline + low contrast
- tertiary - design as links
-

## Layout and spacing

- easiest ways to clean up a design - start with too much whitespace
- dense UIs have their place - dashboards
- linear styles dont work
- have a system => relative difference between adjacent values;
- no two values should be closer than 25%
- start with a sensible base value; build a scale using factors and multiples of that value; lower end is compact; higher end is spaced out
- use the system to design faster; especially spacing and sizing (take the one in refactoring UI)
- dont forcefully fill the screen
- extra space around never hurt anyone; give it the space it needs; you dont need to make it match
- shrink the canvas - it's easier; for responsive, design the mobile layout first
- think in columns
- grids are overrated;
- forcing everything to be fluid - is a mistake
- only shrink a component, if it needs to shrink
- relative sizing doesn't scale (large elements on smaller screens need to shrink faster than the smaller elements)
- connected components have less space between them

## Establish a type scale

- use a hand-crafted scale
- use a design system
- avoid fractional sizes
- avoid em units; stick to px or rem.
- use good fonts
- play it safe - neutral: helvetica
- ignore typefaces with less than 5 weights; crank it up to 10+ on google fonts
- optimize for legibility
- headlines: tight letter spacing, short x height (futura)
- body: wider letter space + taller lowercase (proxima)
- trust the wisdom of the crowd; if it's popular, it's good; sort by popularity
- steal
- develop your intuition
- keep your line length in check: 45-75 chars length; em relative to current font size 20-35em
- vertical align by baseline
- line-height 1.5; is proportional
- line-height and font-size are inversely proportional
- not every link needs a color
- dont center long form text; headlnes or short independent blocks 1-2 lines are ok; more than that, left-align
- right align numbers (get the decimals aligned)
- justify text with hyphenation
- letter-spacing: mostly leave alone
- tighten headlines
- headline fonts rarely work in body
- increase letter space for all-caps

## working with color

- use HSL (hue saturation and lightness)
- hue => position on the color wheel
- saturation => how vivid the color is; 0 is grey, 100 is intense
- lightness => how close to white or black - 100% is pure white, 0 is pure black
- color palette has 3 categories
- greys: text, background, panels, form controls
- darkest grey
- dark grey
- grey
- light grey
- lightest grey
- you'll need 10 greys
- primary color
- primary action, active navigation element
- 5-10 light to dark shades
- accent colors
- destructive actions
- eye-grabbing
- yellow for warnings
- greens for positive trends
- ten different colors with 5-10 different shades
- define your shades upfront
- how to put together a palette
- choose a base color (pick something that works well as a button background) - darkest reserved for text, lightest as a background (think alerts)
- base color - adjust saturation and lightness
- fill in the gaps
- increase saturation as lightness goes up;
- rotate the hue to make it lighter (dont rotate by more than 20-30 degrees)
- greys
- cool greys => saturate with blue
- warm greys => saturate with yellow
- neutral greys => 0 saturation
- contrast ratio
- small text => 4.5:1
- large test => 3:1
- dont rely on color alone (color blindness)
- reinforce with color, don't make it the only communication available

## Creating depth

- emulate a light source: light comes from above
- box-shadow: inset 0 1px 0 hsl(...) \[choose a lighter color by hand\]
- box-shadow:  0 1px 3px hsla(..)
- closer something feels to the user, more it'll attract focus
- dropdowns + buttons + inset input boxes
- large shadows => dialogs
- 5 options for elevations
- mix with interactions
- two shadows (refer to the book)
- creating depth with color
- lighter than the background, appears elevated
- darker = further away
- short vertically offset shadows, no blur radius
- overlap elements to create layers
- image on image overlap - give it an invisible border

## Working with images

- use high quality stock images
- Dont design using placeholder images; it doesn't work
- Text needs consistent contrast. All images will not work as background OR add a black overlay or lower the image contrast or lower the contrast of the image itself or colorize the image
- Dont scale up icons - everything has an intended size; for small icons, keep them in a shaded circle or something
- Don’t scale down screenshots; take a screenshot at a smaller screen size and use that; or it gets cramped; or consider a partial screenshot; or draw a simplified version; blur the details out
- Redraw icons (favicons); control the compromises
- User uploaded content
- Control shape and size; center images in fixed containers, cropping things out
- Prevent background bleed with subtle inner box shadow or semi transparent inner border

## Finishing touches

- Do simple things - bullets => icons
- Quotes to visual elements
- Forms => custom checkboxes and radio buttons; use brand color instead of browser defaults
- Add colors with accent borders
- Play with backgrounds
- Change the background color - add gradients (2 hues not more than 30 degrees aprt)
- Try a repeating pattern ([https://heropatterns.com/](https://heropatterns.com/))
- Add a simple shape or illustration
- Or simplified world map
- Don't overlook empty states
- Use fewer borders
- Add spacing
- Use multiple background colors
- Think outside the box

## how to get better / leveling up

1.  notice decisions you wouldn't have made yourself
2.  rebuild favorite interfaces (WITHOUT looking into developer tools)
