function findFloor() {
    let low = 0;
    let high = arr.length - 1;
    let floor = -1; // Default case if no floor is found

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (arr[mid] <= x) {
            floor = arr[mid]; // Found a new potential floor
            low = mid + 1; // Look for a higher floor to the right
        } else {
            high = mid - 1; // Look to the left
        }
    }

    return floor;
}

module.exports = findFloor