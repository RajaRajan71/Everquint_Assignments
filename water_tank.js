/**
 * Function to calculate trapped rainwater and water levels for visualization.
 * Uses the O(n) time complexity approach (Max Left / Max Right pre-calculation).
 * @param {number[]} heights - Array of block heights.
 * @returns {object} - { totalWater: number, waterLevels: number[] }
 */
function calculateTrappedWater(heights) {
    const n = heights.length;
    if (n < 3) return { totalWater: 0, waterLevels: new Array(n).fill(0) };

    let maxLeftArr = new Array(n).fill(0);
    let maxRightArr = new Array(n).fill(0);
    let totalWater = 0;
    let waterLevels = new Array(n).fill(0);

    // 1. Pre-calculate Max Left array
    let maxLeft = 0;
    for (let i = 0; i < n; i++) {
        maxLeft = Math.max(maxLeft, heights[i]);
        maxLeftArr[i] = maxLeft;
    }

    // 2. Pre-calculate Max Right array
    let maxRight = 0;
    for (let i = n - 1; i >= 0; i--) {
        maxRight = Math.max(maxRight, heights[i]);
        maxRightArr[i] = maxRight;
    }

    // 3. Calculate Water and Total
    for (let i = 0; i < n; i++) {
        // Water trapped = min(MaxL, MaxR) - Current Height
        const waterHeight = Math.min(maxLeftArr[i], maxRightArr[i]) - heights[i];
        if (waterHeight > 0) {
            totalWater += waterHeight;
            waterLevels[i] = waterHeight; // Store level for visualization
        }
    }
    
    return { totalWater, waterLevels };
}

/**
 * Main function called from the HTML button click to run the calculation and visualization.
 */
function runVisualization() {
    const inputElement = document.getElementById('heights-input');
    const resultElement = document.getElementById('water-result');
    const svgContainer = document.getElementById('water-tank-svg');
    
    // Clear previous results
    svgContainer.innerHTML = ''; 
    resultElement.textContent = '...';

    // Parse input (must handle the comma-separated string)
    const heights = inputElement.value
        .split(',')
        .map(s => parseInt(s.trim()))
        .filter(n => !isNaN(n) && n >= 0);

    if (heights.length === 0) {
        resultElement.textContent = 'Invalid Input';
        return;
    }

    // 1. Calculate the result
    const { totalWater, waterLevels } = calculateTrappedWater(heights);

    // 2. Display the total water
    resultElement.textContent = totalWater + ' Units';

    // 3. Generate the visualization
    generateSVGVisualization(heights, waterLevels);
}


/**
 * Generates and appends SVG elements for the blocks and water to the DOM.
 */
function generateSVGVisualization(heights, waterLevels) {
    const svg = document.getElementById('water-tank-svg');
    
    // Configuration for scaling the visualization
    const BAR_WIDTH = 30;
    const SPACING = 5;
    const SCALE = 20; // Pixels per unit height
    const MAX_HEIGHT = Math.max(...heights, 1) + 1; 
    const SVG_HEIGHT = MAX_HEIGHT * SCALE;
    const SVG_WIDTH = heights.length * (BAR_WIDTH + SPACING) + SPACING;

    // Set SVG dimensions
    svg.setAttribute('width', SVG_WIDTH);
    svg.setAttribute('height', SVG_HEIGHT);
    
    // Draw elements
    heights.forEach((height, index) => {
        const x_pos = index * (BAR_WIDTH + SPACING) + SPACING;
        const waterHeight = waterLevels[index];
        
        // --- 1. Draw the Block (Wall) ---
        if (height >= 0) {
            const blockHeight_px = height * SCALE;
            const blockY_pos = SVG_HEIGHT - blockHeight_px; // SVG y-coordinates start from top
            
            const block = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
            block.setAttribute('x', x_pos);
            block.setAttribute('y', blockY_pos);
            block.setAttribute('width', BAR_WIDTH);
            block.setAttribute('height', blockHeight_px);
            block.setAttribute('fill', '#FFC300'); // Yellow/Orange
            svg.appendChild(block);
        }

        // --- 2. Draw the Water ---
        if (waterHeight > 0) {
            // Water level is relative to the *top* of the combined block and water level
            const waterLevelHeight = waterHeight * SCALE;
            const blockTopY = SVG_HEIGHT - (height * SCALE); 
            const waterY_pos = blockTopY - waterLevelHeight;

            const water = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
            water.setAttribute('x', x_pos);
            water.setAttribute('y', waterY_pos);
            water.setAttribute('width', BAR_WIDTH);
            water.setAttribute('height', waterLevelHeight);
            water.setAttribute('fill', '#007FFF'); // Blue
            water.setAttribute('opacity', 0.7);
            svg.appendChild(water);
        }
    });
}
window.onload = runVisualization; // Run automatically on load