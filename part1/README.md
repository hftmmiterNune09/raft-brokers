# RAFT based ATM network
Note that no user is present in the begining. We have to add users from the admin acount

# RUN 3 ATM TERMINALS
    command
        └──bash atm1.sh
        └──bash atm2.sh
        └──bash atm3.sh

# ALLOWED OPERATIONS
    admin:
        └──add usename $money     /* add user in the system with initial money */
        └──rm username            /* remove user from the system */
        └──ls                     /* list user in the system */
    users:
        └──chuser username        /* change user */
        └──wd $money              /* withdraw money from current user */
        └──dp $money              /* deposit money to the current user */
        └──bal                    /* check balance of the current user */
        └──trto otheruser $money  /* transfer $money from current user to other user */

# Contact Me

This is Assignment 3, part 1 of CS60002: Distributed Systems course in IIT Kharagpur, taught by [Dr. Sandip Chakraborty](https://cse.iitkgp.ac.in/~sandipc/). For questions and general feedback, contact [Prasenjit Karmakar](https://www.linkedin.com/in/prasenjit52282).