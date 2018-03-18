var currentSurveyIndex = 0;

$(document).ready(function() {
var surveyJSON = {
 completedHtml: "<div class=\"circle-loader\">\n  <div class=\"checkmark draw\"></div>\n</div>\n\n<div class=\"survey-done-text\">\n  <div class=\"survey-non-questions\">\n    <h4>Thank you for completing our survey!</h4>\n    <p>As a token of our gratitude, here is a code unlocking a 15% discount to our conference in May where the results will be presented in cooperation with KPMG.</p>\n    <p class=\"code\">CFO15P</p>\n    <div class=\"center\">\n      <a class=\"button\" id=\"survey-done-register\" href=\"http://www.cfo-insights.org/denmark/\">Register now</a>\n    </div>\n    <p>If you have any questions or enquiries, feel free to contact us at <a href=\"mailto:contact@cfoinsights.org\">contact@cfoinsights.org</a> </p>\n  </div>\n</div>",
 loadingHtml: "<div class=\"circle-loader\">\n  <div class=\"checkmark draw\"></div>\n</div>",
 pages: [
  {  
     "name":"Priorities",
     "elements":[  
        {  
           "type":"sortablelist",
           "name":"priorities",
           "title":"To what degree do you prioritise the following areas on your agenda as a CFO? (Rank by drag n' drop in a descending order from highest to smallest priority)",
           "isRequired":true,
           "choices":[  
              "Cost Management and Efficiency",
              "Regulatory Compliance",
              "Governance and Stakeholder Management",
              "Strategy",
              "Value Creation and Growth",
              "Digitalization",
              "Risk Management",
           ]
        },
        {
          type: "text",
          name: "Other",
          title: "Other priorities",
          placeHolder: "Please elaborate!"
        }
     ]
  },
  {
   name: "Cost Management & Efficiency",
   elements: [
    {
     type: "matrix",
     name: "Cost Mangement and Efficiency",
     title: "To what degree are the following factors challenging for you in terms of cost management? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Reporting and transparency",
      "Cost variability",
      "Offshoring and nearshoring",
      "Outsourcing",
      "Automation",
      "Cost efficiency"
     ]
    },
    {
     type: "text",
     name: "question8",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Cost Management and Efficiency'",
   title: "Cost Management and Efficiency"
  },
  {
   name: "Regulatory Compliance",
   elements: [
    {
     type: "matrix",
     name: "question2",
     title: "To what degree are the following factors challenging for you in terms of regulatory compliance? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Adopting regulation in the organisation",
      "Adopting regulation in systems & technology ",
      "Adopting regulation in business processes ",
      "Turning regulation into an advantage",
      "Turning regulation into innovation"
     ]
    },
    {
     type: "text",
     name: "question9",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Regulatory Compliance'",
   title: "Regulatory Compliance"
  },
  {
   name: "Governance & stakeholder management",
   elements: [
    {
     type: "matrix",
     name: "question1",
     title: "To what degree are the following factors challenging for you in terms of cost management? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Reporting and transparency",
      "Cost variability",
      "Offshoring and nearshoring",
      "Outsourcing",
      "Automation",
      "Cost efficiency"
     ]
    },
    {
     type: "text",
     name: "question10",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Governance and Stakeholder Management'",
   title: "Governance & stakeholder management "
  },
  {
   name: "Strategy",
   elements: [
    {
     type: "matrix",
     name: "strategy",
     title: "To what degree are the following factors challenging for you in terms of strategy? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Defining vision and direction",
      "Goal setting",
      "Alignment among CXOs",
      "Communication and embedment",
      "Breakdown and operationalisation"
     ]
    },
    {
     type: "text",
     name: "question11",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Strategy'",
   title: "Strategy"
  },
  {
   name: "Value Creation & Growth",
   elements: [
    {
     type: "matrix",
     name: "question3",
     title: "To what degree are the following factors challenging for you in terms of value creation? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Understanding internal value drivers ",
      "Understanding external value drivers ",
      "Foster and drive innovation",
      "Capitalize on future trends",
      "Unclear value propositions",
      "Lack of transparency",
      "Merger & acquisitions ",
      "Post-merger integration "
     ]
    },
    {
     type: "text",
     name: "question12",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Value Creation and Growth'",
   title: "Value Creation & Growth"
  },
  {
   name: "Risk management ",
   elements: [
    {
     type: "matrix",
     name: "Risk management",
     title: "To what degree are the following factors challenging for you in terms of risk management? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Financial risks",
      "Operational risks",
      "Risk mitigation",
      "Cybersecurity",
      "Accountability for risk management",
      "Cooperation between risk, compliance and legal ",
      "Reporting of risks"
     ]
    },
    {
     type: "text",
     name: "question13",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   visible: false,
   visibleIf: "{priorities} highest_ranking 'Risk Management'",
   title: "Risk Management"
  },
  {
   name: "Opportunities and Maturity. ",
   elements: [
    {
     type: "html",
     name: "question4",
     html: "<p><strong>Example:</strong> To what degree is Blockchain an opportunity for your organization?</p>\n\n<p><strong>Example:</strong> To what degree is your organization sufficiently mature for effective implementation of AI and Machine Learning?</p>"
    },
    {
     type: "matrixdropdown",
     name: "Technology - opportunity and maturity",
     title: "Technology - opportunity and maturity.",
     isRequired: true,
     columns: [
      {
       name: "Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation."
      },
      {
       name: "Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity."
      }
     ],
     choices: [
      1,
      2,
      3,
      4,
      5,
      "N/A",
     ],
     cellType: "radiogroup",
     rows: [
      "Cybersecurity",
      "Robotics",
      "Data & Analytics",
      "Cloud Computing",
      "AI & Machine Learning",
      "Blockchain",
      "Digital Assistants (chat/voice)",
      "Internet of Things (sensor/devices)",
      "Augmented & Virtual Reality"
     ]
    }
   ],
   title: "Opportunities and Maturity",
  },
  {
   name: "Digitalisation Opportunities  ",
   elements: [
    {
     type: "matrix",
     name: "To what degre do you see digitalisation as an opportunity to increase efficiency on the following areas? (Rate 1 - 5) ",
     title: "To what degre do you see digitalisation as an opportunity to increase efficiency on the following areas? (Rate 1 - 5) ",
     isRequired: true,
     columns: [
      "1 - Not an opportunity",
      "2 - A minor opportunity",
      "3 - An opportunity",
      "4 - A considerable opportunity",
      "5 - A major opportunity",
      "N/A"
     ],
     rows: [
      "Administration processes",
      "Shorter lead time",
      "Improved quality and consistency",
      "Higher regulative agility",
      "Effective customer interface",
      "Procurement to pay",
      "Order to cash",
      "Record to report"
     ]
    },
    {
     type: "matrix",
     name: "question5",
     title: "To what degre do you see digitalisation as an opportunity to increse value creation on the following areas? (Rate 1 - 5)",
     isRequired: true,
     columns: [
      "1 - Not an opportunity",
      "2 - A minor opportunity",
      "3 - An opportunity",
      "4 - A considerable opportunity",
      "5 - A major opportunity",
      "N/A"
     ],
     rows: [
      "New offerings",
      "Stronger customer interaction",
      "Data Driven decision making",
      "Disrupt competition",
      "Improved brand image"
     ]
    },
    {
     type: "text",
     name: "Other",
     title: "Other possible opportunities",
     placeHolder: "Please elaborate!"
    }
   ],
   title: "Digitalisation Opportunities "
  },
  {
   name: "Digitalization Challenges",
   elements: [
    {
     type: "matrix",
     name: "question6",
     title: "To what degree do you believe the following cultural factors are challenges to effective digitalisation?",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Adaptability to change",
      "Employee digital skills",
      "Organisation and governance",
      "Fear of redundancy ",
      "CXO level of digital capabilities"
     ]
    },
    {
     type: "matrix",
     name: "question7",
     title: "To what degree do you believe the following aspects are challenges to effective digitalisation?",
     isRequired: true,
     columns: [
      "1 - Not a challenge",
      "2 - A minor challenge",
      "3 - A challenge",
      "4 - A considerable challenge",
      "5 - A major challenge",
      "N/A"
     ],
     rows: [
      "Maturity of new technology",
      "Analog/manual processes",
      "Implementation costs",
      "Digital debt & IT legacy "
     ]
    },
    {
     type: "text",
     name: "question14",
     title: "Other challenges",
     placeHolder: "Please elaborate!"
    }
   ],
   title: "Digitalization Opportunities"
  },
  {
   name: "Contact Permission",
   elements: [
    {
     type: "radiogroup",
     name: "follow-up",
     title: "May CFO Insights contact you to follow up on your questions?",
     choices: [
      "Yes",
      "No"
     ],
     choicesOrder: "desc"
    }
   ],
   title: "Follow-up"
  },
  {
   name: "Contact Information",
   elements: [
    {
     type: "text",
     name: "Your e-mail",
     isRequired: true,
     inputType: "email"
    },
    {
     type: "text",
     name: "Phone number",
     title: "Your phone number (including localization)",
     inputType: "tel"
    }
   ],
   visibleIf: "{follow-up} = 'Yes'",
   title: "Your contact information"
  }
 ]
}

var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sendDataToServer(survey) {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
         type:"POST",
         url:"/denmark/survey/questions/ajax/submit",
         data: {
                'survey_response': JSON.stringify(survey.data)
                },
         success: function(){
              return false;
            }
    });

    window.setTimeout(function() {
        $('.circle-loader').toggleClass('load-complete');
        $('.survey-done-text').toggleClass('survey-done-text-toggled');
        window.setTimeout(function() {
          $('.survey-done-text .survey-non-questions').slideDown('fast');
        }, 1000)
        $('.checkmark').toggle();
      }, 3000);
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    showQuestionNumbers: "OFF",
    onComplete: sendDataToServer
});
});