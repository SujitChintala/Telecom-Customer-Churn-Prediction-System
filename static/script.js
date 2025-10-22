// Form handling and API interaction

document.addEventListener('DOMContentLoaded', function() {
    console.log('Churn Prediction System loaded');
    
    // Initialize tooltips
    initializeTooltips();
    
    // Form submission
    const form = document.getElementById('predictionForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});

/**
 * Initialize tooltips with hover functionality
 */
function initializeTooltips() {
    const tooltips = document.querySelectorAll('.tooltip');
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', function() {
            const title = this.getAttribute('title');
            if (title) {
                this.setAttribute('data-title', title);
                this.removeAttribute('title');
            }
        });
    });
}

/**
 * Handle form submission
 */
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Hide any previous results or errors
    hideResults();
    hideError();
    
    // Show loading spinner
    showLoading();
    
    // Collect form data
    const formData = collectFormData();
    
    try {
        // Make prediction request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        // Hide loading spinner
        hideLoading();
        
        if (data.success) {
            displayResults(data);
        } else {
            displayError(data.error || 'An error occurred during prediction');
        }
        
    } catch (error) {
        hideLoading();
        console.error('Error:', error);
        displayError('Failed to connect to the server. Please try again.');
    }
}

/**
 * Collect form data into an object
 */
function collectFormData() {
    const form = document.getElementById('predictionForm');
    const formData = new FormData(form);
    const data = {};
    
    // Convert FormData to object
    for (let [key, value] of formData.entries()) {
        data[key] = parseFloat(value);
    }
    
    return data;
}

/**
 * Display prediction results
 */
function displayResults(data) {
    const resultsSection = document.getElementById('resultsSection');
    const predictionLabel = document.getElementById('predictionLabel');
    const resultDescription = document.getElementById('resultDescription');
    const resultIcon = document.getElementById('resultIcon');
    const churnProb = document.getElementById('churnProb');
    const notChurnProb = document.getElementById('notChurnProb');
    const churnBar = document.getElementById('churnBar');
    const recommendation = document.getElementById('recommendation');
    
    // Set prediction label and description
    if (data.prediction === 1) {
        predictionLabel.textContent = 'Customer Will Churn';
        predictionLabel.style.color = '#e74c3c';
        resultDescription.textContent = 'High risk of customer churn detected';
        resultIcon.className = 'fas fa-exclamation-circle icon-danger';
    } else {
        predictionLabel.textContent = 'Customer Will Not Churn';
        predictionLabel.style.color = '#27ae60';
        resultDescription.textContent = 'Low risk of customer churn';
        resultIcon.className = 'fas fa-check-circle icon-success';
    }
    
    // Set probabilities
    churnProb.textContent = data.probability.churn + '%';
    notChurnProb.textContent = data.probability.not_churn + '%';
    
    // Animate probability bar
    setTimeout(() => {
        churnBar.style.width = data.probability.churn + '%';
    }, 100);
    
    // Generate recommendations
    const recommendationHTML = generateRecommendations(data);
    recommendation.innerHTML = recommendationHTML;
    
    // Show results section
    resultsSection.style.display = 'block';
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Generate personalized recommendations based on prediction
 */
function generateRecommendations(data) {
    let html = '<h4><i class="fas fa-lightbulb"></i> Recommendations</h4><ul>';
    
    if (data.prediction === 1) {
        // High churn risk recommendations
        html += '<li><strong>Immediate Action Required:</strong> Contact customer retention team</li>';
        html += '<li>Review customer service interactions and resolve any issues</li>';
        html += '<li>Offer personalized retention incentives or discounts</li>';
        html += '<li>Schedule a follow-up call to understand concerns</li>';
        
        // Analyze input features for specific recommendations
        if (data.input_features.CustServCalls >= 4) {
            html += '<li><strong>Alert:</strong> High customer service calls detected - investigate issues</li>';
        }
        if (data.input_features.ContractRenewal === 0) {
            html += '<li><strong>Alert:</strong> Contract not renewed - offer renewal incentives</li>';
        }
        if (data.input_features.OverageFee > 15) {
            html += '<li>Consider upgrading customer to a higher plan to reduce overage fees</li>';
        }
    } else {
        // Low churn risk recommendations
        html += '<li>Customer appears satisfied - maintain current service quality</li>';
        html += '<li>Consider upselling additional services or features</li>';
        html += '<li>Send satisfaction survey to gather feedback</li>';
        html += '<li>Reward loyalty with exclusive offers</li>';
        
        // Positive reinforcement
        if (data.input_features.ContractRenewal === 1) {
            html += '<li><strong>Positive:</strong> Contract renewed - customer shows commitment</li>';
        }
        if (data.input_features.CustServCalls <= 1) {
            html += '<li><strong>Positive:</strong> Low customer service calls - good service experience</li>';
        }
    }
    
    html += '</ul>';
    return html;
}

/**
 * Display error message
 */
function displayError(message) {
    const errorSection = document.getElementById('errorSection');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
    
    // Scroll to error
    errorSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Show loading spinner
 */
function showLoading() {
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'block';
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    const loadingSpinner = document.getElementById('loadingSpinner');
    loadingSpinner.style.display = 'none';
}

/**
 * Hide results section
 */
function hideResults() {
    const resultsSection = document.getElementById('resultsSection');
    resultsSection.style.display = 'none';
}

/**
 * Hide error section
 */
function hideError() {
    const errorSection = document.getElementById('errorSection');
    errorSection.style.display = 'none';
}

/**
 * Reset form to initial state
 */
function resetForm() {
    const form = document.getElementById('predictionForm');
    form.reset();
    hideResults();
    hideError();
    
    // Scroll to top of form
    form.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/**
 * Reset results and show form again
 */
function resetResults() {
    hideResults();
    hideError();
    
    // Scroll to form
    const form = document.getElementById('predictionForm');
    form.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/**
 * Load sample data for testing
 */
function loadSampleData(churnType = 'not_churn') {
    const sampleData = {
        'not_churn': {
            AccountWeeks: 128,
            ContractRenewal: 1,
            DataPlan: 1,
            DataUsage: 2.7,
            CustServCalls: 1,
            DayMins: 265.1,
            DayCalls: 110,
            MonthlyCharge: 89,
            OverageFee: 9.87,
            RoamMins: 10
        },
        'churn': {
            AccountWeeks: 65,
            ContractRenewal: 0,
            DataPlan: 0,
            DataUsage: 0.29,
            CustServCalls: 4,
            DayMins: 129.1,
            DayCalls: 137,
            MonthlyCharge: 44.9,
            OverageFee: 11.43,
            RoamMins: 12.7
        }
    };
    
    const data = sampleData[churnType];
    
    for (let key in data) {
        const element = document.getElementById(key);
        if (element) {
            element.value = data[key];
        }
    }
}

// Validation helpers
function validateForm() {
    const form = document.getElementById('predictionForm');
    return form.checkValidity();
}

// Add input validation feedback
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="number"]');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && !this.checkValidity()) {
                this.style.borderColor = '#e74c3c';
            } else {
                this.style.borderColor = '#ddd';
            }
        });
        
        input.addEventListener('input', function() {
            if (this.checkValidity()) {
                this.style.borderColor = '#27ae60';
            }
        });
    });
});
