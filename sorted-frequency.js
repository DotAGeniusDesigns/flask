function sortedFrequency() {
    function binarySearch(isFirst) {
        let low = 0;
        let high = arr.length - 1;
        let index = -1;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (arr[mid] === num) {
                index = mid; // Found an occurrence
                // Adjust search range based on isFirst flag
                if (isFirst) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (arr[mid] < num) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return index;
    }

    const firstIndex = binarySearch(true);
    if (firstIndex === -1) return -1; // Number not found in the array

    const lastIndex = binarySearch(false);
    return lastIndex - firstIndex + 1;
}

module.exports = sortedFrequency