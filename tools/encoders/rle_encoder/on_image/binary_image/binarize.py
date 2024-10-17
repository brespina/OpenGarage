class BinImage:
    def __init__(self):
        pass

    def get_hist(self, image):

        hist = [0] * 256

        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                hist[image[i][j]] += 1

        return hist

    def thresh(self, hist):
        """
        takes bimod hist as input
        returns (otsu's) threshhold
        """
        total_num_pixels = 0
        intraClassVar = []

        for i in range(len(hist)):
            total_num_pixels += hist[i]

        for j in range(len(hist)):
            size_0 = 0.0
            sum_0 = 0.0
            var_0 = 0.0

            size_T = 0.0
            sum_T = 0.0
            var_T = 0.0

            threshold = j

            # compute stats 1
            for k in range(threshold):
                size_0 += hist[k]
                sum_0 += k * hist[k]

            if size_0 == 0:
                continue

            mean_0 = sum_0 / size_0
            weight_0 = size_0 / total_num_pixels

            for k in range(threshold):
                var_0 += ((k - mean_0) ** 2) * hist[k]

            var_0 /= size_0

            # compute stats 2:
            for m in range(threshold, len(hist)):
                size_T += hist[m]
                sum_T += m * hist[m]

            if size_T == 0:
                continue

            mean_T = sum_T / size_T
            weight_T = size_T / total_num_pixels

            for m in range(threshold, len(hist)):
                var_T += ((m - mean_T) ** 2) * hist[m]

            var_T /= size_T
            intraClassVar.append((weight_0 * var_0 + weight_T * var_T, j))

        best_threshold = min(intraClassVar)[1]

        return best_threshold

    def binarize(self, image):
        """
        takes a grayscale image (no alpha) shape only (height, width)
        returns binary image based on otsu's threshold
        """
        bin_img = image.copy()
        x = BinImage.get_hist(self, image)
        y = BinImage.thresh(self, x)

        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                if image[i][j] < y:
                    bin_img[i][j] = 0
                else:
                    bin_img[i][j] = 255

        return bin_img
