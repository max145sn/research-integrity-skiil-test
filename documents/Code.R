#Title: The Effects of Exposure to Objective Coherence on Perceived Meaning in Life: A Preregistered Direct Replication of Heintzelman, Trent, and King (2013)
#Authors, Year: Ratner, K., Burrow, A. L., & Thoemmes, F. (2016)
#Journal: Royal Society Open Science

#data formatting - read in data from file location
setwd("C:\\Users\\")

st2 <- read.csv("Study2rawdataexp.csv", sep = ',', header=FALSE, skip=3)
st2names <- read.csv("Study2rawdataexp.csv", sep = ',', header=TRUE, nrows=1)
st4 <- read.csv("Study4rawdataexp.csv", sep = ',', header=FALSE, skip=3)
st4names <- read.csv("Study4rawdataexp.csv", sep = ',', header=TRUE, nrows=1)

#put proper variable names back into dataframe
names(st2) <- names(st2names)
names(st4) <- names(st4names)




#Study 2 Formatting
#checking that data was read correctly
head(st2)
nrow(st2)
str(st2)

#Recoding meaning scores and attention check to be on standard likert scale
library(car)
st2$mil1 <- recode(st2$MILCon_15, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")
st2$mil2 <- recode(st2$MILCon_17, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")
st2$mil3 <- recode(st2$MILCon_19, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")
st2$mil4 <- recode(st2$MILCon_21, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")
st2$mil5 <- recode(st2$MILCon_22, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")

st2$check <- recode(st2$MILCon_2, "18=1;19=2;20=3;21=4;22=5;23=6;24=7")

#Designating experimental conditions for S2
#1=Seasonal, 2=arbitrary, 3=random
#always run these 6 lines together
  st2$c1 <- ifelse(st2$RO.BR.FL_15 == "", 999, 1)
  st2$c2 <- ifelse(st2$RO.BR.FL_48 == "", 999, 3)
  st2$c3 <- ifelse(st2$RO.BR.FL_67 == "", 999, 2)
  table(st2$c1, st2$c2,useNA = "always")
  table(st2$c1, st2$c3,useNA = "always")
  table(st2$c2, st2$c3,useNA = "always")
  table(st2$c1, st2$c2, st2$c3, useNA = "always")
  st2$cond <- ifelse(st2$c1==1, 1, 999)
  st2$cond <- ifelse(st2$c2==3, 3, st2$cond) 
  st2$cond <- ifelse(st2$c3==2, 2, st2$cond)

table(st2$cond)


st2$timesum <- rowSums(st2[c(11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 
                             95, 102, 109, 116,123, 130, 137, 144, 151, 158, 
                             165, 172, 179, 186, 193, 200, 207, 214, 221, 228,235, 
                             242, 249, 256, 263, 270, 277, 284, 291, 298, 305, 312, 
                             319, 326, 333, 340,347, 354, 361, 368, 375, 382, 389, 
                             396, 403, 410, 417, 424, 431, 438, 445, 452,459, 466, 
                             473, 480, 487, 494, 501, 508, 515, 522, 529, 536, 543, 
                             550, 557, 564,571, 578, 585, 592, 599, 606, 613, 620, 
                             627, 634, 641, 648, 655, 662, 669, 676,683, 690, 697, 
                             704, 711, 718, 725, 732, 739, 746, 753, 760, 767, 774, 
                             781, 788,795, 802, 809, 816, 823, 830, 837, 844, 851, 
                             858, 865, 872, 879, 886, 893, 900,907, 914, 921, 928, 
                             935, 942, 949, 956, 963, 970, 977, 984, 991, 998, 1005, 
                             1012,1019, 1026, 1033, 1040, 1047, 1054, 1061, 1068, 
                             1075, 1082, 1089, 1096, 1103, 1110, 1117, 1124,1131, 
                             1138, 1145, 1152, 1159, 1166, 1173, 1180, 1187, 1194, 
                             1201, 1208, 1215, 1222, 1229, 1236,1243, 1250, 1257, 
                             1264, 1271, 1278, 1285, 1292, 1299, 1306, 1313, 1320, 
                             1327, 1334, 1341, 1348,1355, 1362, 1369, 1376, 1383, 
                             1390, 1397, 1404, 1411, 1418, 1425, 1432, 1439, 1446, 
                             1453, 1460,1467, 1474, 1481, 1488, 1495, 1502, 1509, 
                             1516, 1523, 1530, 1537, 1544, 1551, 1558, 1565, 1572,
                             1579, 1586, 1593, 1600, 1607, 1614, 1621, 1628, 1635, 
                             1642, 1649, 1656, 1663, 1670, 1677, 1684,1691, 1698, 
                             1705, 1712, 1719, 1726, 1733, 1740, 1747, 1754, 1761, 
                             1768, 1775, 1782, 1789, 1796,1803, 1810, 1817, 1824, 
                             1831, 1838, 1845, 1852, 1859, 1866, 1873, 1880, 1887, 
                             1894, 1901, 1908,1915, 1922, 1929, 1936, 1943, 1950, 
                             1957, 1964, 1971, 1978, 1985, 1992, 1999, 2006, 2013, 
                             2020,2027, 2034, 2041, 2048, 2055, 2062, 2069, 2076, 
                             2083, 2090, 2097, 2104, 2111, 2118, 2125, 2132,2139, 
                             2146, 2153, 2160, 2167, 2174, 2181, 2188, 2195, 2202, 
                             2209, 2216, 2223, 2230, 2237, 2244,2251, 2258, 2265, 
                             2272, 2279, 2286, 2293, 2300, 2307, 2314, 2321, 2328, 
                             2335, 2342, 2349, 2356,2363, 2370, 2377, 2384, 2391, 
                             2398, 2405, 2412, 2419, 2426, 2433, 2440, 2447, 2454, 
                             2461, 2468,2475, 2482, 2489, 2496, 2503, 2510, 2517, 
                             2524, 2531, 2538, 2545, 2552, 2559, 2566, 2573, 2580,
                             2587, 2594, 2601, 2608, 2615, 2622, 2629, 2636, 2643, 
                             2650, 2657, 2664, 2671, 2678, 2685, 2692)],na.rm = TRUE)

st2$timeavg <- st2$timesum / 16

#Making means of the DV and covariates
st2$mil <- rowMeans(st2[,2746:2750], na.rm=TRUE)
st2$epa <- rowMeans(st2[c(2703,2705,2707)], na.rm=TRUE)
st2$ena <- rowMeans(st2[c(2704,2706)], na.rm=TRUE)
st2$ipa <- rowMeans(st2[c(2708, 2710, 2712, 2714, 2716, 2718, 2720, 2722, 2724, 2726, 2728, 2730, 2732, 2734, 2736)], na.rm=TRUE)
st2$ina <- rowMeans(st2[c(2709, 2711, 2713, 2715, 2717, 2719, 2721, 2723, 2725, 2727, 2729, 2731, 2733, 2735, 2737)], na.rm=TRUE)

#Study 2 demographic descriptives
library(psych)

#D2 is age
describe(st2$D2)
#D1 is sex, 1 = male, 2 = female
table(st2$D1)



#transferring selected variables into a new dataframe
s2 <- data.frame(st2$mil, st2$epa, st2$ena, st2$ipa, st2$ina, st2$timesum, st2$timeavg, st2$cond, st2$check)  
names(s2) <- c("mil", "epa", "ena", "ipa", "ina", "timesum", "timeavg", "cond", "check")

#check for missing values
sapply(s2, function(x) sum(is.na(x)))

#check for univariate outliers onoutcome
boxplot(s2$mil)
#delete outliers if necessary

#attention check
table(s2$check)

#delete individuals who failed attention check
s2$checkbin <- ifelse(s2$check!=1,1,0)
s2 <- s2[s2$checkbin==0,]
s2$cond <- as.factor(s2$cond)

table(s2$cond)

#Descriptive stats on remaining cases
tapply(s2$mil, s2$cond, describe)
describe(s2$mil)

tapply(s2$epa, s2$cond, describe)
describe(s2$epa)

tapply(s2$ena, s2$cond, describe)
describe(s2$ena)

tapply(s2$ipa, s2$cond, describe)
describe(s2$ipa)

tapply(s2$ina, s2$cond, describe)
describe(s2$ina)

tapply(s2$timesum, s2$cond, describe)
describe(s2$timesum)



#Preregistered Analyses, Study 2
#unadjusted treatment effect
aov1 <- aov(s2$mil ~ s2$cond)
summary(aov1)

#checking for homogeneity of variance in overall ANOVA model
#homogeneity of variance holds
leveneTest(mil~cond,data=s2)
library(HH)
hovPlot(mil~cond, data =s2)

#checking order of condition levels
levels(s2$cond)
#Levene's test for the contrasted two groups
leveneTest(s2$mil,factor(ifelse(s2$cond==3,1,0)))
#applying contrast to test average of seasonal and arbitrary vs. random
library(gmodels)
fit.contrast(aov1, s2$cond, c(.5, .5, -1), conf.int=.95)

#partial eta-squared for condition variable of overall model
library(lsr)
etaSquared(aov1, type = 1, anova = TRUE)

#Cohen's d for contrasted model
library(compute.es)
table(ifelse(s2$cond==3,1,0))
tes(fit.contrast(aov1, s2$cond, c(.5, .5, -1), conf.int=.95)[1,3],318,160)



#regression showing 100% exact same analysis as ANOVA with custom contrast
codes <-  matrix(c(1/3, 1/2, 
                   1/3, -1/2, 
                   -2/3, 0), ncol = 2,byrow=TRUE)
codes
contrasts(s2$cond) <- codes
contrasts(s2$cond)

s2unadj <- lm(mil~cond,data=s2)
summary(s2unadj)



#adjusted effect
s2adj <- lm(mil~cond+epa+ena+ipa+ina+timesum, data=s2)
plot(s2adj)
summary(s2adj)
confint(s2adj)

#creating hand-coded contrast variables for semi-partial
s2$contra1 <- ifelse(s2$cond==1,1/3,NA)
s2$contra1 <- ifelse(s2$cond==2,1/3,s2$contra1)
s2$contra1 <- ifelse(s2$cond==3,-2/3,s2$contra1)
s2$contra2 <- ifelse(s2$cond==1,.5,NA)
s2$contra2 <- ifelse(s2$cond==2,-.5,s2$contra2)
s2$contra2 <- ifelse(s2$cond==3,0,s2$contra2)

#these results are identical to above, but contra1 and contra2 are spelled out so that lsr packages works
s2adjb <- lm(mil~contra1+contra2+epa+ena+ipa+ina+timesum, data=s2)
summary(s2adjb)

#semi-partial R^2
library(lsr)
etaSquared(s2adjb)



#Bayesian Analyses
library(BayesFactor)

#unadjusted effect, overall ANOVA
baov1 <- anovaBF(mil ~ cond,data=s2)
summary(baov1)


#unadjusted effect using hand coded contrasts 
#and then getting at Bayes Factor for particular focal hypothesis
  s2$contra1 <- ifelse(s2$cond==1,1/3,NA)
  s2$contra1 <- ifelse(s2$cond==2,1/3,s2$contra1)
  s2$contra1 <- ifelse(s2$cond==3,-2/3,s2$contra1)
  s2$contra2 <- ifelse(s2$cond==1,.5,NA)
  s2$contra2 <- ifelse(s2$cond==2,-.5,s2$contra2)
  s2$contra2 <- ifelse(s2$cond==3,0,s2$contra2)


bs2_a <- lmBF(mil~contra1+contra2, data=s2)
bs2_b <- lmBF(mil~contra2, data=s2)

bs2_a / bs2_b


#adjusted effect using hand coded contrasts
#and then getting Bayes Factor for particular focal hypothesis
bs2adj_c <- lmBF(mil~contra1+contra2+epa+ena+ipa+ina+timesum, data=s2)
bs2adj_d <- lmBF(mil~contra2+epa+ena+ipa+ina+timesum, data=s2)

bs2adj_c / bs2adj_d


#########################################################

#Study 4
#study 4 data formatting
head(st4)
str(st4)
nrow(st4)

#renaming the attention check
st4$check <- st4$MLQ_6

#recoding reverse-coded MLQ item
st4$MLQ_5r <- recode(st4$MLQ_5, "7=1;6=2;5=3;3=5;2=6;1=7")

#creating means for every participant, DVs and covariates
st4$mil <- rowMeans(st4[c(110:113, 126)], na.rm=TRUE)
st4$epa <- rowMeans(st4[c(116,118,120)], na.rm=TRUE)
st4$ena <- rowMeans(st4[c(117,119)], na.rm=TRUE)

#recoding condition
#Coherent = 0, Incoherent = 1
st4$cond <- ifelse(st4$RO.BR.FL_9=="Coherent",0,1)

table(st4$cond)

#Study 4 descriptives
#Again, 1 = male, 2 = female
table(st4$D1)
#D2 is age
describe(st4$D2)




#transferring relevant variables into clean dataframe
s4 <- data.frame(st4$cond, st4$mil, st4$epa, st4$ena, st4$check)
names(s4) <- c("cond", "mil", "epa", "ena", "check")

#check for missing values
sapply(s4, function(x) sum(is.na(x)))

#check for univariate outliers onoutcome
boxplot(s4$mil)
#delete outliers if necessary

#attention check
table(s4$check)

#delete individuals who failed attention check
s4$checkbin <- ifelse(s4$check!=1,1,0)
s4 <- s4[s4$checkbin==0,]
s4$cond <- as.factor(s4$cond)

#Study descriptives of remaining cases
table(s4$cond)

describe(s4$mil)
tapply(s4$mil, s4$cond, describe)

tapply(s4$epa, s4$cond, describe)
describe(s4$epa)

tapply(s4$ena, s4$cond, describe)
describe(s4$ena)




#Preregistered analyses, Study 4
#unadjusted treatment effect
leveneTest(s4$mil, s4$cond)
#Levene's test not significant - Welch adjustment is not needed
t.test(mil~cond,data=s4, var.equal = T)
#effect size
library(effsize)
cohen.d(s4$mil~s4$cond)

#adjusted effect
s4adj <- lm(mil~cond+epa+ena,data=s4)
summary(s4adj)
confint(s4adj)
plot(s4adj)

#condition effect size in adjusted model
etaSquared(s4adj)

#Bayesian analysis
#unadjusted effect
baov2 <- anovaBF(mil~cond,data=s4)
summary(baov2)
#adjusted treatment effect
bs4adj_a <- lmBF(mil~cond+epa+ena,data=s4)
bs4adj_b <- lmBF(mil~epa+ena,data=s4)

bs4adj_a / bs4adj_b



###########################################################################


#Unregistered exploratory analyses
#Adjusted effect, Study 2 using timeavg instead of preregistered timesum
#averages are just linear transforms of sums, so nothing changes
#therefore we are not rerunning everything
codes <-  matrix(c(1/3, 1/2, 
                   1/3, -1/2, 
                   -2/3, 0), ncol = 2,byrow=TRUE)
codes
contrasts(s2$cond) <- codes
contrasts(s2$cond)

s2adjexp <- lm(mil~cond+epa+ena+ipa+ina+timeavg, data=s2)
summary(s2adjexp)
confint(s2adjexp)

#post-hoc probing of bad looking residuals
#this regression suggested some violations of linearity
library(car)
s2adj <- lm(mil~cond+epa+ena+ipa+ina+timesum, data=s2)
par(mfrow=c(2,2))
plot(s2adj)
summary(s2adj)
par(mfrow=c(1,1))
qqPlot(s2adj, ylab = "Studentized Residuals") #qqplot shows many resids out of 95% CI
hist(resid(s2adj)) #hist shows resids that are skewed
hist(s2$mil) #possibly due to outcome variable being skewed as well

#exploring bi-variate non-linearities between all explanatory variables and the outcome
scatter.smooth(jitter(s2$epa),jitter(s2$mil))
scatter.smooth(jitter(s2$ena),jitter(s2$mil))
scatter.smooth(jitter(s2$ipa),jitter(s2$mil))
scatter.smooth(jitter(s2$ina),jitter(s2$mil))
scatter.smooth(jitter(s2$timesum),jitter(s2$mil),xlim=c(0,500))

#a model with saturated interactions and all quad terms
#also excluding outliers on time, and one outlier (455 who had large Cook's D)
#still pretty similar in terms of residuals
s2test <- s2[s2$timesum<500,]
s2adj2 <- lm(mil~cond+epa+ena+ipa+ina+timesum+I(timesum^2)+I(ina^2)+I(ipa^2)+I(ena^2)+I(epa^2)+
               cond*epa+cond*ena+cond*ipa+cond:ina+ina*cond+cond*timesum, data=s2test[-455,])
par(mfrow=c(2,2))
plot(s2adj2)
summary(s2adj2)
hist(s2adj2$residuals)

#trying to exlude terms to see whether one might be responible
#none of these residuals looks very good
plot(lm(mil~cond,data=s2test))
plot(lm(mil~cond+epa,data=s2test))
plot(lm(mil~cond+ena,data=s2test))
plot(lm(mil~cond+ina,data=s2test))
plot(lm(mil~cond+timesum,data=s2test))

#trying boxcox - optimal 
boxCox(lm(mil~cond+epa+ena+ina+timesum,data=s2test))
s2test$miltrans <- s2test$mil^1.5
plot(lm(miltrans~cond+epa+ena+ina+timesum,data=s2test))
summary(lm(miltrans~cond+epa+ena+ina+timesum,data=s2test))


#conducting meta-analysis of effects
library(metafor)

#study 1, unadjusted effect
#taken from Table 1, reported as d=.49
oes1unadj <- escalc(measure = "SMD",m1i = 5.08,m2i = 4.36,sd1i = 1.47, sd2i = 1.53,n1i = 38, n2i = 39)

#study 1, adjusted effect
#taken from description of standardized regression coefficient of .21, p = .049
#first we derive standard deviation of the dummy coded variables that was used
sd(c(rep(1,38),rep(0,39))) #sd of dummy code
#now transform standardized coefficients to unstandardized coefficients
#we do this by dividing the standardized coefficients by the product of standard deviations of both predictor and outcome
#the standard deviation of the outcome is from Table 2
unstb1adj <- .21 / sd(c(rep(1,38),rep(0,39)))*1.54
#from this it follows that the adjusted mean difference between seasonal and random is .643
oes1adj <- escalc(measure = "SMD",m1i = unstb1adj,m2i = 0,sd1i = 1.47, sd2i = 1.53,n1i = 38, n2i = 39)


#study 2, unadjusted effect
#original effect, weighted mean, and weighted variance for combined group
#results were taken from Table 2 of original paper, and seasonal and arbitrary patterns were combined
#i.e., we formed weighted means and weighted variances of the two groups
(oes2unadj <- escalc(measure = "SMD",m1i = 5.1297,m2i = 4.56,sd1i = 1.316, sd2i = 1.75,n1i = 90, n2i = 47))
#our effect from replication study 
tapply(s2$mil,(ifelse(s2$cond==3,1,0)),mean)
tapply(s2$mil,(ifelse(s2$cond==3,1,0)),sd)
(res2unadj <- escalc(measure = "SMD",m1i = 4.739465,m2i = 4.644687,sd1i = 1.615522, sd2i = 1.755500,n1i = 318, n2i = 160))
#meta-analysis results study2
rma(rbind(oes2unadj$yi,res2unadj$yi),rbind(oes2unadj$vi,res2unadj$vi))

#study 2, adjusted effect
#original effect, using regression coefficients reported in text
#regression coefficients appear to be standardized, but is actually not specified in text
#first we derive standard deviation of the two dummy coded variables that were used
sd(c(rep(1,46),rep(0,44+47))) #sd of first dummy code
sd(c(rep(1,44),rep(0,46+47))) #sd of second dummy code
#now transform standardized coefficients to unstandardized coefficients
#we do this by dividing the standardized coefficients by the product of standard deviations of both predictor and outcome
#the standard deviation of the outcome is from Table 2
unstb1 <- .17 / sd(c(rep(1,46),rep(0,44+47)))*1.49 
unstb2 <- .19 / sd(c(rep(1,44),rep(0,46+47))) *1.49 
#from this it follows that the mean differences between seasonal and random is .534, 
#and the difference between arbitrary and random is .604
#therefore a combined weighted mean difference between season + arbitrary vs random is (.534*46 + .604*44) / 90 = 0.568
(oes2adj <- escalc(measure = "SMD",m1i = .568,m2i = 0,sd1i = 1.316, sd2i = 1.75,n1i = 90, n2i = 47))
#the adjusted effect in our study follows directly from the unstandardized regression coefficient and the associated 
#standard deviation of the groups that are being compared
(res2adj <- escalc(measure = "SMD",m1i = 0.1444022,m2i = 0,sd1i = 1.615522, sd2i = 1.755500,n1i = 318, n2i = 160))

#meta-analysis results study2 adjusted effects
rma(rbind(oes2adj$yi,res2adj$yi),rbind(oes2adj$vi,res2adj$vi))


#study 3, unadjusted effect
#means and SD directy from text, reported d in text = .54
(oes3unadj <- escalc(measure = "SMD",m1i = 5.40,m2i = 4.81,sd1i = .89, sd2i = 1.32,n1i = 30, n2i = 30))

#study 3, adjusted effect
#derived from standardized beta weight .27, p = .02
#first we derive standard deviation of the dummy coded variable
sd(c(rep(1,30),rep(0,30))) #sd of first dummy code
#now transform standardized coefficients to unstandardized coefficients
#we do this by dividing the standardized coefficients by the product of standard deviations of both predictor and outcome
#the standard deviation of the outcome is from text 1.17
unstb3 <- .27 / sd(c(rep(1,30),rep(0,30)))*1.17 
(oes3adj <- escalc(measure = "SMD",m1i = unstb3,m2i = 0,sd1i = .89, sd2i = 1.32,n1i = 30, n2i = 30))


#study 4, unadjusted effect
#directly from table 3
(oes4unadj <- escalc(measure = "SMD",m1i = 4.90,m2i = 4.24,sd1i = 1.49, sd2i = 1.49,n1i = 85, n2i = 84))
#our effect directly from our own descriptive stats
tapply(s4$mil, s4$cond, mean)
(res4unadj <- escalc(measure = "SMD",m1i = 4.680208,m2i = 4.833333,sd1i = 1.64, sd2i = 1.44,n1i = 144, n2i = 147))
rma(rbind(oes4unadj$yi,res4unadj$yi),rbind(oes4unadj$vi,res4unadj$vi))


#study 4, adjusted effect
#we again unstandardize coefficient that is reported by using the standard deviations of the dummy code and the outcome
unstb4 <- .14 / sd(c(rep(0,85),rep(1,84)))*1.52 
(oes4adj <- escalc(measure = "SMD",m1i = unstb4,m2i = 0,sd1i = 1.49, sd2i = 1.49,n1i = 85, n2i = 84))

#from our own replication study we can use the unstandardized regression coefficient
(res4adj <- escalc(measure = "SMD",m1i = 0.01638,m2i = 0,sd1i = 1.64, sd2i = 1.44,n1i = 144, n2i = 147))
#and final meta-analysis of adjusted effect of study 4
rma(rbind(oes4adj$yi,res4adj$yi),rbind(oes4adj$vi,res4adj$vi))




#meta-analysis of all unadjusted effects
rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
    rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi))

ovsr <- c(0,0,0,0,1,1)
tvsw <- c(0,0,1,1,0,1)


funnel(rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
           rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi)))

funnel(rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
           rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi)),refline=0)

plot(rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
           rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi)),refline=0)



#meta-analysis of all unadjusted effects with moderators
rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
    rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi),
    mods = cbind(ovsr,tvsw))

rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
    rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi),
    mods = cbind(ovsr))

rma(rbind(oes1unadj$yi,oes2unadj$yi,oes3unadj$yi,oes4unadj$yi,res2unadj$yi,res4unadj$yi),
    rbind(oes1unadj$vi,oes2unadj$vi,oes3unadj$vi,oes4unadj$vi,res2unadj$vi,res4unadj$vi),
    mods = cbind(tvsw))

#meta-analysis of all adjusted effects
rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
    rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi))

plot(rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
    rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi)))


plot(rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
         rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi)),refline=0)



funnel(rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
         rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi)),refline=0)


#meta-analysis of all adjusted effects with mods
rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
    rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi),
    mods = cbind(ovsr,tvsw))

rma(rbind(oes1adj$yi,oes2adj$yi,oes3adj$yi,oes4adj$yi,res2adj$yi,res4adj$yi),
    rbind(oes1adj$vi,oes2adj$vi,oes3adj$vi,oes4adj$vi,res2adj$vi,res4adj$vi),
    mods = cbind(ovsr))
