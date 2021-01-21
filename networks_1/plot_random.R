#!/bin/env Rscript

library(ggplot2)

data = read.csv("random_walk.csv")

iter = 1000

var = 1/2

data$gauss = 1/sqrt(2 * pi * var * iter) * exp(-data$pos^2/(4 * iter * var))

chart <- ggplot(data, aes(x = pos))
chart + geom_point(aes(y=prob)) + geom_line(aes(y=gauss))
ggsave(paste("random_walk", iter, ".png"))
