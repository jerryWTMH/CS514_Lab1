   
import sabre

class CustomReplacement(sabre.Replacement):
    def check_replace(self, quality):
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()
        buffer = self.session.get_buffer_contents()
        available = 0
        for index, bitrate in enumerate(bitrates):
            if bitrate <= throughput:
                available = index
            else:
                break
        for i in range(2, len(buffer)):
            if buffer[i] < available:
                # return -ve index from end of buffer
                return (i - len(buffer), available)
        # if we arrive here, no switching occurs
        return (None, 0)
