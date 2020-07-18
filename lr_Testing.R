#testing with http://www.omdbapi.com/?i=tt0096697&Season=4&apikey=7259c64b
raw <- read.csv("lr_testing.csv")
names(raw) <- c("Rating", "Episode", "predict")
raw$Episode <- 1:nrow(raw)

results <- lm(raw$Rating ~ raw$Episode)
plot(Rating ~ Episode, raw)
lines(raw$Episode, predict(results), col = "blue")

plot(results$fitted.values)
