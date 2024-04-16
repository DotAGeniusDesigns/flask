function findRotatedIndex() {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (arr[mid] === num) return mid;

        // Check if the left side is sorted
        if (arr[low] <= arr[mid]) {
            if (num >= arr[low] && num <= arr[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else { // Right side must be sorted
            if (num >= arr[mid] && num <= arr[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }

    return -1;
}

module.exports = findRotatedIndex