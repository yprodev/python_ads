# Implementation of the main simulation class
from array import Array
from '../queue_linked_list' import Queue
from passenger import TicketAgent, Passenger

class TicketCounterSimulation:
	# Create a simulation object
	def __init__(self, numAgents, numMinutes, betwwenTime, serviceTime):
		# Parameters supplied by the user
		self._arriveProb = 1.0 / betwwenTime
		self._serviceTime = serviceTime
		self._numMinutes = numMinutes

		# Simulation components
		self._passengerQ = Queue()
		self._theAgents = Array(numAgents)

		for i in range(numAgents):
			self._theAgents[i] = TicketAgent(i + 1)

		# Computed during the simulation
		self._totalWaitTime = 0
		self._numPassengers = 0

	# Run the simulation using the parameters supplied earlier
	def run(self):
		for curTime in range(self._numMinutes + 1):
			self._handleArrival(curTime)
			self._handleBeginService(curTime)
			self._handleEndService(curTime)

	# Print the simulation results
	def printResults(self):
		numServed = self._numPassengers - len(self._passengerQ)
		avgWait = float(self._totalWaitTime) / numServed

		print(" ")
		print("Number of passengers served = ", numServed)
		print("Number of passengers remaining in line = %d " % len(self._passengerQ))
		print("The avarage wait time was %4.2f minutes" % avgWait)


	# The remaining methods that have yet to be implemented
	def _handleArrive(curTime): # Handles simulation rule #1
	def _handleBeginService(curTime): # Handles simulation rule #2
	def _handleEndService(curTime): # Handles simulation rule #3








