    def fancy(self, time_allowance=60.0):
        results = {}
        start_time = time.time()
        count = 0

        randomResults = self.defaultRandomTour()
        bssf = randomResults['soln']


        route = bssf.route
        improveFactor = 1
        improveThreshHold = .00001
        upBound = bssf.cost

        while improveFactor > improveThreshHold:
            boundToBeat = upBound
            for i in range(1, len(route) - 1):
                for j in range(i + 1, len(route) - 1):
                    newRoute = self.twoOptSwap(route, i, j)
                    newSolution = TSPSolution(newRoute)

                    if newSolution.cost < upBound:
                        route = newRoute
                        upBound = newSolution.cost
                        count += 1

            improveFactor = 1 - upBound/boundToBeat

        end_time = time.time()
        results['cost'] = upBound
        results['time'] = end_time - start_time
        results['count'] = count
        results['soln'] = TSPSolution(route)
        results['max'] = 0
        results['total'] = 0
        results['pruned'] = 0
        return results
      
    def twoOptSwap(self, route, i, k):
        newRoute = []
        # newRoute = np.concatenate((route[0:i], route[k:-len(route) + i - 1:-1], route[k + 1:len(route)]))
        for ind1 in range(i):
            newRoute.append(route[ind1])
        for ind2 in range(k, i - 1, -1):
            newRoute.append(route[ind2])
        for ind3 in range(k + 1, len(route)):
            newRoute.append(route[ind3])

        return newRoute
