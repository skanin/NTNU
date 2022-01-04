library(ggplot2)

df <- read.csv('~/Documents/it3028/synthetic-data.csv')

# Histogram
ggplot(df, aes(x=posts)) + geom_histogram()

# Density plot
ggplot(df, aes(x=posts)) + geom_density()

library('gridExtra')

newDf <- data.frame(value = c(df$happy, df$sad, df$angry), variable = rep(c('happy', 'sad', 'angry')))

ggplot(newDf, aes(x=value)) + geom_density() + facet_wrap(.~variable)

# scatter plot

ggplot(df, aes(x=mid.term, y=final_score, colour=pre.test)) + geom_point() + stat_smooth(method = 'lm', se=FALSE)
names(df)


# mean plot
# install.packages('plyr')
library('gplots')
library('plyr')

df$newPriorKnowledge <- mapvalues(df$pre.test, from=levels(factor(df$pre.test)), to=c('1.high', '3.low', '2.medium'))

plotmeans(df$final_score~df$pre.test)
plotmeans(df$final_score~df$newPriorKnowledge)

# Chi-square

tab1 <- table(df$GENDER, df$pre.test)

chisq.test(tab1)

# t-test



