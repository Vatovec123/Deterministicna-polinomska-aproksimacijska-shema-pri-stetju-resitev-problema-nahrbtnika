library(readxl)

#5 predmetov in 10 poiskusov
tabela1 <- data.frame(read_excel("Uvoz/5predmetov.xlsx",na = "n.a." ), row.names = c("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."))
colnames(tabela1) <- c("Poiskus","Epsilon 0.08", "Epsilon 0.1", "Epsilon 0.3", "Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9")
tabela1[1] <- NULL

tabela1 <- t(tabela1)

#10 predmetov in 10 poiskusov
tabela2 <- data.frame(read_excel("Uvoz/10predmetov.xlsx",na = "n.a." ), row.names = c("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."))
colnames(tabela2) <- c("Poiskus", "Epsilon 0.1", "Epsilon 0.3", "Epsilon 0.5", "Epsilon 0.7", "Epsilon 0.9")
tabela2[1] <- NULL

tabela2 <- t(tabela2)

#20 predmetov in 10 poiskusov
tabela3 <- data.frame(read_excel("Uvoz/20predmetov.xlsx",na = "n.a." ), row.names = c("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."))
tabela3[1] <- NULL

tabela3 <- t(tabela3)

#5 predmetov in 50 poiskusov
tabela4 <- data.frame(read_excel("Uvoz/5predmetov_50poskusov.xlsx",na = "n.a." ), row.names = c(1:50))
tabela4[1] <- NULL

tabela4 <- t(tabela4)


# Razlika do točnih rezultatov_ 10 predmetov 
tabela5 <- data.frame(read_excel("Uvoz/odstopanja_10predmetov.xlsx",na = "n.a." ), row.names = c("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."))
tabela5[1] <- NULL

# Razlika do točnih rezultatov - 20 predmetov
tabela6 <- data.frame(read_excel("Uvoz/odstopanja_20predmetov.xlsx",na = "n.a." ), row.names = c("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10."))
tabela6[1] <- NULL



