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

##### Fourier Analysis

Fourier analysis is a field of mathematics concerned with understanding how arbitrary functions can be represented as a superposition of simple periodic functions. Modern Fourier analysis is an extension of the concept of Fourier series; if a general function can be approximated by a combination of regular periodic functions then studying these component functions can reveal properties of the original function. In this way, a Fourier transform can convert time-series data into the frequency domain and then provide information on the amplitude and phase of these underlying frequencies.

### Background

##### Fourier Series

A Fourier series F(x) is the representation of an arbitrary periodic function f(x) as a sum of trigonometric functions. The trigonometric functions most commonly used to construct the sum are the Sine and Cosine functions, this is called the sine-cosine form of the Fourier series (Equation 1.1). The sum is calculated using the coefficients a<sub>0</sub>, a<sub>n</sub> and a<sub>b</sub> (Equations 1.2 - 1.4) over an analysis period P = P<sub>1</sub> - P<sub>2</sub>.

{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/eq1_1.png" caption="Equation 1.1" width="415" height="79" %}
{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/eq1_2.png" caption="Equation 1.2" width="201" height="79" %}
{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/eq1_3.png" caption="Equation 1.2" width="320" height="79" %}
{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/eq1_4.png" caption="Equation 1.2" width="360" height="79" %}

Figure 1 demonstrates the approximation of a sawtooth function by a Fourier series, the two functions typically become equal as N is increased towards infinity.

{% include figure.html image="https://tarkanbilge.github.io/assets/learn/fourier/fig_1.png" caption="Figure 1" width="415" height="79" %}
