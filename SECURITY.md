# Security

This document explains the security implemented into HealthBox, and its limitations.


## Summary

In short, HealthBox prioritizes your security, and places privacy at its core design. However, you shouldn't trust it to be bullet proof, and should still use reasonable discretion when configuring HealthBox.

**HealthBox should never be used in situations where safety is dependent on reliable access to health information.**


## Privacy

In terms of privacy, HealthBox makes absolutely no compromises. All of your information is hosted in your HealthBox instance, which is entirely open source. HealthBox works completely independent of the internet, and no information is ever sent to external servers without you explicitly configuring it to do so.


## Information Security

HealthBox takes information security very seriously. However, it's important to know its limitations. Here are some things to keep in mind:

- The HealthBox database is encrypted, but this encryption is only as strong as the password you use to encrypt it. An app that can crack this password can access your health data. If this occurs, HealthBox will be unable to tell it is happening, nor will it be able to log it.
- A strong database password means practically nothing if the malicious program is running locally, on the same machine that you host HealthBox with. A malicious program can monitor your keyboard inputs and record your password as you enter it while initializing HealthBox. For this reason, you should only install programs you trust on your computer.
- Your information is only as secure as its weakest link. While HealthBox itself is encrypted, an program or device that submits information to HealthBox over the internet may do so in an unencrypted fashion. If this is the case, the program submitting information becomes the weakest link, and anyone attempting to snoop on your health information would be able to intercept the data while it is in transit to HealthBox.


## Most Secure Configurations

The most secure configuration for HealthBox depends on what you trust more: The devices and software you use with HealthBox, or the people on your network.

If you trust the devices and software you use with HealthBox more, then the most secure configuration for you would likely be to run HealthBox and the programs that communicate with it on the same machine. This would allow you to block network requests to HealthBox, ensuring it can't be accessed externally. This would prevent remote devices from being able to communicate with HealthBox, but would thwart potential attackers looking to remotely compromise your HealthBox instance.

If you trust the people on your network more, the more secure configuration for you may involve setting up your HealthBox instance on a server seperate from your main devices. For example, you may want to run HealthBox on a Raspberry Pi. This means that programs and devices connecting to HealthBox won't have direct access to it, making it harder for them to tamper with it. However, this exposes your HealthBox instance to everyone on your local network, or even the entire internet if you configure it as such. Therefore, if security is a serious concern, you should only use this configuration on a home network, or other environment where you trust all the users on your network.


## Reliability

HealthBox is engineered to fail safe, even at the expense of reliability. For this reason, **HealthBox should absolutely not be used in situations where safety is dependent on being able to access health information**. For example, HealthBox works great for keeping track of your diet as you try to get in shape, but should not be used for a patient in a hopstial recovering from surgery, where exact portions and timing are critical to their safety.

While HealthBox does its best to handle malformed data submitted to its API, it's relatively easy for an adversary to crash it. Rather than attempt to parse malformed data, and potentially exposure security, issues, HealthBox will panic and close if it encounters something it doesn't understand what to do with. This improves security, but can compromise reliability. It should be noted that the reliability of HealthBox should improve over time, as more edge cases are implemented.


## Reporting Security Issues

If you discover security problems related to HealthBox, I highly encourage you to contact [V0LT support](mailto:cvieira@v0lttech.com) so I can make sure users are made aware of the issue, and it gets solved as soon as possible!
