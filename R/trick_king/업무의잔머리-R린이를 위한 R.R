# install.packages("ggplot2")
library("ggplot2")

mpg

MPG <- as.data.frame(ggplot2::mpg)

ggplot(MPG,aes(cty,hwy)) + geom_point()
ggplot(MPG,aes(cty,hwy)) + geom_point(alpha=0.1)
ggplot(MPG,aes(cty,hwy)) + geom_count()

ggplot(MPG,aes(drv,hwy,color=drv)) + geom_boxplot() + geom_hline(yintercept = 25, color="orange")

library("dplyr")
MPG_F <- MPG %>% filter(drv=="f" | drv =="r")
table(MPG_F$drv)
ggplot(MPG_F,aes(drv,hwy,color=drv)) + geom_boxplot() + geom_hline(yintercept = 25, color="orange")

MPG_G <- MPG %>% group_by(drv) %>% summarise(AV=mean(hwy),Max=max(hwy),Min=min(hwy))
MPG_G <- MPG %>% filter(drv=="f" | drv =="r") %>%
  group_by(drv) %>% summarise(AV=mean(hwy),Max=max(hwy),Min=min(hwy))
MPG_S <- MPG %>% select(drv,cty,hwy)
