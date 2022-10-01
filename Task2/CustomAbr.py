import sabre

class CustomAbr(sabre.Abr):
    def __init__(self, config):
        super().__init__(config)
        # Your variables here:
        self.myQ = 0

    def get_quality_delay(self, segment_index):
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()
        buffers = self.session.get_buffer_contents()
        quality = self.myQ
        while (quality + 1 < len(bitrates) and abs(quality - self.myQ) < 2 and 
               bitrates[quality + 1] <= throughput):
            quality += 1
        self.myQ = quality
        return (quality, 0)
