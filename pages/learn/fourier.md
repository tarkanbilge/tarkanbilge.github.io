---
title: Fourier Analysis
feature_text: |

feature_image: "https://tarkanbilge.github.io/assets/mountain1.jpg"
excerpt: "Fourier Analysis"
aside: false
---

### Introduction

##### Purpose

This article is intended to introduce Fourier analysis as a tool for the frequency analysis of time-series data. There is some background provided on Fourier Series and on the different types of Fourier transform, this is aimed at giving the reader a clearer idea of how Fourier analysis works, but will include no mathematical derivations.
After that, the focus of this article will be on applying the Discrete Fourier Transform (DFT), and on an extension to this method known as the Multitaper method. All visualisations and accompanying scripts are freely available in the Github repository.

Fourier analysis is a field of mathematics concerned with understanding how arbitrary functions can be represented as a superposition of simple periodic functions. Modern Fourier analysis is an extension of the concept of Fourier series; if a general function can be approximated by a combination of regular periodic functions then studying these component functions can reveal properties of the original function. In this way, a Fourier transform can convert time-series data into the frequency domain and then provide information on the amplitude and phase of these underlying frequencies.

### Background

##### Fourier Series

A Fourier series is the representation of an arbitrary periodic function as a sum of trigonometric functions. The trigonometric functions most commonly used to construct the sum are the Sine and Cosine functions, this is called the sine-cosine form of the Fourier series (Equation 1).

{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/eq1.png" caption="Equation 1" width="415" height="79" %}
