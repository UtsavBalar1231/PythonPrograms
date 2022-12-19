class Disk:
    """
    this class initializes the disk size, position and array of requests
    """
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.requests = []
        
    def add_request(self, request):
        """
        add a request to the array of requests
        """
        self.requests.append(request)

    def print_requests(self):
        """
        print out the array of requests
        """
        print("Requests: ", end='')
        for i in range(len(self.requests)):
            print(self.requests[i], end=' ')
        print()
        
    def print_position(self):
        """
        print out the current position of the disk
        """
        print("Current position: ", self.position)
        
    def print_size(self):
        """
        print out the size of the disk
        """
        print("Disk size: ", self.size)
        
    def print_all(self):
        """
        print out all the information about the disk
        """
        self.print_size()
        self.print_position()
        self.print_requests()
        
    def FCFS(self):
        """
        First Come First Serve
        """
        print("First Come First Serve")
        self.print_all()

        total = 0
        # Iterate through the requests
        for i in range(len(self.requests)):
            # print the movement from the current position to the next request
            print("Move from {} to {}".format(self.position, self.requests[i]))
            # add the distance moved to the total
            total += abs(self.position - self.requests[i])
            self.position = self.requests[i]

        # print the total distance moved
        print("Total head movement: ", total)
        print()
        
    def SSTF(self):
        """
        Shortest Seek Time First
        """
        print("Shortest Seek Time First")
        self.print_all()

        total = 0
        # Iterate through the requests until there are no more requests
        while len(self.requests) > 0:
            # Find the request with the shortest distance from the current position
            min = abs(self.position - self.requests[0])
            index = 0
            # Iterate through the requests
            for i in range(len(self.requests)):
                # If the distance from the current position to the request is less than the current minimum
                if abs(self.position - self.requests[i]) < min:
                    # Set the minimum to the new minimum
                    min = abs(self.position - self.requests[i])
                    index = i
                    
            # print the movement from the current position to the next request
            print("Move from {} to {}".format(self.position, self.requests[index]))
            # add the distance moved to the total
            total += abs(self.position - self.requests[index])
            # set the current position to the request
            self.position = self.requests[index]
            # remove the request from the array of requests
            self.requests.pop(index)
        print("Total head movement: ", total)
        print()
        
    def SCAN(self):
        """
        Elevator SCAN
        """
        print("Elevator SCAN")
        self.print_all()
        
        total = 0
        # Sort the requests in ascending order
        self.requests.sort()
        
        index = 0
        # Find the index of the first request that is greater than the current position
        for i in range(len(self.requests)):
            if self.requests[i] > self.position:
                index = i
                break
        
        # Iterate through the requests from the index to the end of the array
        for i in range(index, len(self.requests)):
            # print the movement from the current position to the next request
            print("Move from {} to {}".format(self.position, self.requests[i]))
            # add the distance moved to the total
            total += abs(self.position - self.requests[i])
            # set the current position to the request
            self.position = self.requests[i]           
        print("Move from {} to 0".format(self.position))
        # add the distance moved to the total
        total += self.position
        self.position = 0
        # Iterate through the requests from the beginning of the array to the index
        for i in range(index):
            # print the movement from the current position to the next request
            print("Move from {} to {}".format(self.position, self.requests[i]))
            # add the distance moved to the total
            total += abs(self.position - self.requests[i])
            # set the current position to the request
            self.position = self.requests[i]
        print("Total head movement: ", total)
        print()
        
    def CSCAN(self):
        """
        Circular SCAN
        """
        print("Circular SCAN")
        self.print_all()
        
        total = 0
        # Sort the requests in ascending order
        self.requests.sort()

        index = 0
        # Find the index of the first request that is greater than the current position
        for i in range(len(self.requests)):
            if self.requests[i] > self.position:
                index = i
                break
            
        # Iterate through the requests from the index to the end of the array
        for i in range(index, len(self.requests)):
            # print the movement from the current position to the next request
            print("Move from {} to {}".format(self.position, self.requests[i]))
            # add the distance moved to the total
            total += abs(self.position - self.requests[i])
            # set the current position to the request
            self.position = self.requests[i]
        print("Move from {} to 0".format(self.position))
        # add the distance moved to the total
        total += self.position
        self.position = 0
        print("Move from {} to {}".format(self.position, self.size - 1))
        total += self.size - 1

        # set the current position to the end of the disk
        self.position = self.size - 1
        # Iterate through the requests from the beginning of the array to the index
        for i in range(index):
            print("Move from {} to {}".format(self.position, self.requests[i]))
            total += abs(self.position - self.requests[i])
            self.position = self.requests[i]
        print("Total head movement: ", total)
        print()
               
if __name__ == "__main__":
    disk = Disk(5000, 143)
    disk.add_request(86)
    disk.add_request(1470)
    disk.add_request(913)
    disk.add_request(1774)
    disk.add_request(948)
    disk.add_request(1509)
    disk.add_request(1022)
    disk.add_request(1750)
    disk.add_request(130)
    
    disk.FCFS()
    disk.SSTF()
    disk.SCAN()
    disk.CSCAN()