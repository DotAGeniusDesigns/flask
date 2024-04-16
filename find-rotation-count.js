function findRotationCount() {
    let low = 0;
    let high = arr.length - 1;

    while (low < high) {
        if (arr[low] < arr[high]) {
            return low; // This means the array is not rotated at all
        }

        let mid = Math.floor((low + high) / 2);

        // Check if the element at mid is the minimum
        if (arr[mid] < arr[mid - 1]) {
            return mid;
        } else if (arr[mid + 1] < arr[mid]) {
            return mid + 1;
        }

        // Determine which half to search
        if (arr[mid] > arr[high]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return low;
}

module.exports = findRotationCount