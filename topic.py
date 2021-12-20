import producer
import consumer

prod = producer
con = consumer

#Input your topic here
prod.producer("mumbai")
con.consumer("mumbai")