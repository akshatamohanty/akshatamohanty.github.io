---
title: "How to make an animated navigation component using Angular?"
description: Getting started with Angular Animations by building a simple component
date: 2018-04-25
layout: post
tag:
  - web-and-performance
  - angularjs
---

Animations are an important part of the user experience. The subtle movements in an app, when done right, not only provide the user with useful feedback but also create an unconscious, favourable impression of 'smoothness' in your application/website. Angular provides a way to add animations to your app, tied to your application logic, with almost similar performance as native CSS animations.

## tl;dr recipe

- Import BrowserAnimationsModule and add it to imports in **_app.module.ts_**
- Import { trigger, state, style, transition, animate, keyframes } from '@angular/animations'
- Add an animation in the **animations** array of the Component
- Define states and add function in the component.ts file to switch between states
- Add [@animation_name] to an element in your HTML and give it a value controlled by component

## Adding an animation

#### Installing Angular Animations Package

Make sure you have @angular/animations installed, using `npm install @angular/animations --save`.

**_package.json_**

```
"dependencies": {
    ...
    "@angular/animations": "^5.2.10",
    ...

```

#### Importing the Browser Animation Module

The BrowserAnimationsModule is part of the **@angular/platform-browser** package. The platform-browser is automatically installed if you've generated your app using angular-cli. Only the BrowserAnimationsModule will need to be imported and added to the **imports** array, as shown below.

**_app.module.ts_**

```
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  ...
  imports: [
    BrowserAnimationsModule,
    ...
  ]
  ...
})
export class AppModule { }
```

#### Importing required animation functions in the component

To add animations to your component, you will need to add metadata defining your animation while creating your component. To define your animation, you'll need to minimally import

- trigger
- state
- style
- transition
- animate
- keyframes

**_app.component.ts_**

```
import { trigger, state, style, transition, animate, keyframes } from '@angular/animations';
```

#### Adding an animation to the component

In the example below, the metadata has defined an animation trigger, called "slide*in_out" with two states - 'slide_in' and 'slide_out'. The states can be considered as the values the animation \_slide_in_out* can be assigned and the corresponding CSS that becomes active on getting that value.

The transition is what specifies the animation when the states changes from slide_in to slide_out and vice versa. You can choose to define this animation in one direction, from void / any state, with different timing and effects.

**_app.component.ts_**

```
@Component({
  ...
  animations: [
    trigger('slide_in_out', [
      state('slide_in', style({
        width: '350px',
        // css styles when the element is in slide_in
      })),
      state('slide_out', style({
        width: '0px'
        // css styles when the element is in slide_out
      })),
      // animation effect when transitioning from one state to another
      transition('slide_in <=> slide_out', animate(300))
    ]),
  ]
})
```

#### Add the animation to the element

Once you've defined your animation, you can now add it to your HTML element and link it to a variable, slider_state in this example. In this example, when the slider_state equals 'slide_in', the width of the div is 350px and when the slider_state equals 'slide_out', the width of the div is 0.

The slider_state variable needs to be controlled in your component file. In this example, we control the slide-in-out navbar using a button.

When the button is clicked, it changes the value of slider_state, as shown below, hence triggering the animation.

**_app.component.html_**

```html
<button (click)="toggleSlider()">Toggle Slider</button>

<div id="slide-nav" [@slide_in_out]="slider_state">
  <!-- some content -->
</div>
```

**_app.component.ts_**

```ts
  slider_state:string = "slide_in";
  toggleSlider(): void{
    // do something to change the animation_state variable
    this.slider_state = this.slider_state === 'slide_out' ? 'slide_in' : 'slide_out';
  }
```

And that's it. That's how you implement a simple slide-in, slide-out sidenav. View a demo [here](https://stackblitz.com/edit/angular-slide-nav?file=app%2Fapp.module.ts)

## Pitfalls

- web-animations-js is required to make an angular animation work in browsers that donot support the **Web Animations API**
- The state is defined as a **string** value and use booleans or numerical values might cause errors

#### References:

[Angular Animations Documentation](https://angular.io/guide/animations)
