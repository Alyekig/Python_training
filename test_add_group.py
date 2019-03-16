{
  "id": "9aa3cb67-4de7-4446-982f-eb9eb0d4f9e4",
  "version": "2.0",
  "name": "Adress book",
  "url": "http://127.0.0.1",
  "tests": [{
    "id": "f158179e-eccf-4c98-ad13-ca4d1e87bf27",
    "name": "test",
    "commands": [{
      "id": "25928f20-5865-4875-b8a1-5199316f48c2",
      "comment": "",
      "command": "open",
      "target": "/addressbook/",
      "targets": [],
      "value": ""
    }, {
      "id": "078feb68-473c-4358-a0b4-b2c0e8a3fb90",
      "comment": "",
      "command": "setWindowSize",
      "target": "452x686",
      "targets": [],
      "value": ""
    }, {
      "id": "124c8484-4285-481f-a641-926cec29bc54",
      "comment": "",
      "command": "type",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "admin"
    }, {
      "id": "6d14e5d2-398c-4943-a2d6-c5b6190bb7e0",
      "comment": "",
      "command": "click",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f8070b5f-113b-47db-b845-278fa407e494",
      "comment": "",
      "command": "type",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": "secret"
    }, {
      "id": "fbb49b65-54d1-42b3-8a79-fa222bd972e6",
      "comment": "",
      "command": "click",
      "target": "css=input:nth-child(7)",
      "targets": [
        ["css=input:nth-child(7)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[3]", "xpath:idRelative"],
        ["xpath=//input[3]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "41e15d11-11e9-4284-8f85-e4521c01e86a",
      "comment": "",
      "command": "click",
      "target": "linkText=groups",
      "targets": [
        ["linkText=groups", "linkText"],
        ["css=.admin > a", "css:finder"],
        ["xpath=//a[contains(text(),'groups')]", "xpath:link"],
        ["xpath=//div[@id='nav']/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'group.php')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'groups')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "187f653b-8b2d-4b1b-b105-0bfa494f4f95",
      "comment": "",
      "command": "click",
      "target": "name=new",
      "targets": [
        ["name=new", "name"],
        ["css=form:nth-child(2) > input:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='new']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6d571568-cc89-4f7d-b6b1-088b486a2b67",
      "comment": "",
      "command": "click",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "02291286-07ce-4595-a5d9-e64f7b618422",
      "comment": "",
      "command": "type",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": "Test"
    }, {
      "id": "267c0799-16e9-49c1-bdc1-4e2b52bb6b3f",
      "comment": "",
      "command": "click",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(9)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "180c2f52-d089-406a-ae87-56cbc90ccc49",
      "comment": "",
      "command": "type",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(9)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": "test"
    }, {
      "id": "ddfbb991-0d86-42a5-a253-e3d4607a49b9",
      "comment": "",
      "command": "click",
      "target": "name=group_footer",
      "targets": [
        ["name=group_footer", "name"],
        ["css=textarea:nth-child(12)", "css:finder"],
        ["xpath=//textarea[@name='group_footer']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea[2]", "xpath:idRelative"],
        ["xpath=//textarea[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9c6d5712-e25b-46f5-b6c0-1340ed0f47f0",
      "comment": "",
      "command": "type",
      "target": "name=group_footer",
      "targets": [
        ["name=group_footer", "name"],
        ["css=textarea:nth-child(12)", "css:finder"],
        ["xpath=//textarea[@name='group_footer']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea[2]", "xpath:idRelative"],
        ["xpath=//textarea[2]", "xpath:position"]
      ],
      "value": "test"
    }, {
      "id": "a581126a-2919-4d76-a064-cc3a6ee1b5ad",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(15)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9489b819-8c49-4a64-bc33-f94f626adec7",
      "comment": "",
      "command": "click",
      "target": "linkText=Logout",
      "targets": [
        ["linkText=Logout", "linkText"],
        ["css=a:nth-child(3)", "css:finder"],
        ["xpath=//a[contains(text(),'Logout')]", "xpath:link"],
        ["xpath=//a[@onclick='document.logout.submit();']", "xpath:attributes"],
        ["xpath=//div[@id='top']/form/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '#')]", "xpath:href"],
        ["xpath=//a", "xpath:position"],
        ["xpath=//a[contains(.,'Logout')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "89d7d4fe-8fd3-49fb-9ab3-782858ec77e5",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["f158179e-eccf-4c98-ad13-ca4d1e87bf27"]
  }],
  "urls": ["http://127.0.0.1/"],
  "plugins": []
}