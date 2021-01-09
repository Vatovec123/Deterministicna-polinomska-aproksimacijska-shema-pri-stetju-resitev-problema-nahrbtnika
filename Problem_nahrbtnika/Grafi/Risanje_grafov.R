# 5 predmetov in 10 poiskusov
library(broman)

colors1 <- colors <- c( brocolors("crayons")["Indigo"], brocolors("crayons")["Violet Red"],  brocolors("crayons")["Maroon"],  brocolors("crayons")["Lemon Yellow"],brocolors("crayons")["Granny Smith Apple"], brocolors("crayons")["Piggy Pink"])

png("Grafi/5predmetov.png")
barplot(tabela1,beside = T, ylim=c(0,5),xlab="Število poskusov",ylab="Čas [s]", col=colors1,axis.lty="solid" )
lbls1 <- c("Epsilon 0.08", "Epsilon 0.1", "Epsilon 0.3", "Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9")
legend(51,5, lbls1, fill = colors, ncol = 1, cex = 0.7,  text.font = 4, bty = "n")
dev.off()

# 10 predmetov in 10 poiskusov
colors2 <- c( brocolors("crayons")["Indigo"], brocolors("crayons")["Violet Red"],  brocolors("crayons")["Maroon"],  brocolors("crayons")["Lemon Yellow"],brocolors("crayons")["Granny Smith Apple"])

png("Grafi/10predmetov.png")
barplot(tabela2,beside = T, ylim=c(0,60),xlab="Število poskusov",ylab="Čas [s]", col=colors2,axis.lty="solid" )
lbls2 <- c("Epsilon 0.1", "Epsilon 0.3", "Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9")
legend(1.6,63,lbls2, fill = colors1, ncol = 1, cex = 0.7,  text.font = 4, bty = "n")
dev.off()

# 20 predmetov in 10 poiskusov
colors3 <- c( brocolors("crayons")["Indigo"], brocolors("crayons")["Violet Red"],  brocolors("crayons")["Maroon"])

png("Grafi/20predmetov.png")
barplot(tabela3,beside = T, ylim=c(0,70),xlab="Število poskusov",ylab="Čas [s]", col=colors3,axis.lty="solid" )
lbls3 <- c("Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9")
legend(34,67,lbls3, fill = colors3, ncol = 1, cex = 0.7,  text.font = 4, bty = "n")
dev.off()


# Razlika do točnih vrednosti- 10 predmetov
colors5 <- c( brocolors("crayons")["Jungle Green"], brocolors("crayons")["Denim"],  brocolors("crayons")["Orange"], brocolors("crayons")["Granny Smith Apple"], brocolors("crayons")["Lemon Yellow"])

png("Grafi/odstopanje10.png")
graf1 <- plot(tabela5$epsilon01, type = "l", col = brocolors("crayons")["Jungle Green"], xlab = "Poskus", ylab = "Razlika do prave vrednosti",
                  cex.main = 1,ylim = c(0,6),  lwd = 3)
axis(1, at = seq(1,10))
points(tabela5$epsilon01,col = brocolors("crayons")["Jungle Green"], pch = 1 )
lines(tabela5$epsilon03, col = brocolors("crayons")["Denim"], lwd = 3)
points(tabela5$epsilon03,col = brocolors("crayons")["Denim"], pch = 1 )
lines(tabela5$epsilon05, col = brocolors("crayons")["Orange"], lwd = 3)
points(tabela5$epsilon05,col = brocolors("crayons")["Orange"], pch = 1 )
lines(tabela5$epsilon07, col = brocolors("crayons")["Granny Smith Apple"], lwd = 3)
points(tabela5$epsilon07,col = brocolors("crayons")["Granny Smith Apple"], pch = 1 )
lines(tabela5$epsilon09, col = brocolors("crayons")["Lemon Yellow"], lwd = 3)
points(tabela5$epsilon09,col = brocolors("crayons")["Lemon Yellow"], pch = 1 )
text(x = c(5,1.5, 3, 5, 2.2), y = c(1, 0.4, 4.4,1.8, 5.5), labels = c("Epsilon 0.1", "Epsilon 0.3","Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9"), col = colors5)
dev.off()


png("Grafi/odstopanje20.png")
graf2 <- plot(tabela6$epsilon01, type = "l", col = brocolors("crayons")["Jungle Green"], xlab = "Poskus", ylab = "Razlika do prave vrednosti",
              cex.main = 1,ylim = c(10,170),  lwd = 3, xlim = c(1,10))
axis(1, at = seq(1,10))
points(tabela6$epsilon01,col = brocolors("crayons")["Jungle Green"], pch = 1 )
lines(tabela6$epsilon03, col = brocolors("crayons")["Denim"], lwd = 3)
points(tabela6$epsilon03,col = brocolors("crayons")["Denim"], pch = 1 )
lines(tabela6$epsilon05, col = brocolors("crayons")["Orange"], lwd = 3)
points(tabela6$epsilon05,col = brocolors("crayons")["Orange"], pch = 1 )
lines(tabela6$epsilon07, col = brocolors("crayons")["Granny Smith Apple"], lwd = 3)
points(tabela6$epsilon07,col = brocolors("crayons")["Granny Smith Apple"], pch = 1 )
lines(tabela6$epsilon09, col = brocolors("crayons")["Lemon Yellow"], lwd = 3)
points(tabela6$epsilon09,col = brocolors("crayons")["Lemon Yellow"], pch = 1 )
text(x = c(2,7, 3, 9, 2), y = c(15, 45, 55,92, 150), labels = c("Epsilon 0.1", "Epsilon 0.3","Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9"), col = colors5)
dev.off()
