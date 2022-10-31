#This is a 

search2 <- function(list, item, returndata = FALSE) {
    min <- 0
    max <- length(list)
    prevs <- matrix(ncol = 2)
    while(TRUE) {
        cursor <- as.integer(ceiling((min + max) / 2))
        dist <- abs(cursor-item)
        prevs <- rbind(prevs, c(cursor, dist))
        if (list[cursor]  < item) {
            min <- cursor
        } else if (list[cursor]  > item) {
            max <- cursor
        } else if (returndata) {
            prevs <- prevs[-1, ]
            return(prevs)
        } else {
            return(cursor)
        }
        }
    }




g <- list()

for (i in 1:10000) {
    g <- append(g, i)
}

vals <- search2(g, 51, returndata = TRUE)

plot(1:nrow(vals), vals[,2], "l", xlab = "Step", ylab = "Distance From Value")
