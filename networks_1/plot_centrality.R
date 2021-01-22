#!/bin/env Rscript
data = read.csv("undirected_centrality.csv")
library(ggplot2)
chart <- ggplot(data, aes(x = density)) + geom_line(aes(y = deg.betw, col = "deg-betw")) + geom_line(aes(y = deg.close, col="deg-close")) + geom_line(aes(y = deg.katz, col = "deg-katz")) + geom_line(aes(y = close.betw, col = "close-betw")) + geom_line(aes(y = close.katz, col = "close.katz")) + geom_line(aes(y = betw.katz, col = "betw-katz"))

chart + theme_classic() + xlab("Matrix density") + ylab("Pearson Correlation") + ggtitle("Correlation of different centrality measures for varying graph connectivity")

ggsave("undirected_centrality.png")

