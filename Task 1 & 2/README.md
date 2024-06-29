# Continuous Deployment

## Introduction

For task 1 & 2, I initially decided to use AWS CloudFormation. However, after successfully deploying my CloudFormation template, I wanted to explore other tools such as Ansible and Terraform. The following paragraphs detail my experience and logic while completing these tasks.

## Using CloudFormation

**URL:** [http://static-website-updated2-851725612577-ap-southeast-2.s3-website-ap-southeast-2.amazonaws.com/](http://static-website-updated2-851725612577-ap-southeast-2.s3-website-ap-southeast-2.amazonaws.com/)

I started with CloudFormation as I was more familiar with AWS services and tools than Azure, GCP, or Terraform.

### Logic

Here is the logic breakdown behind the CloudFormation template I developed: 
1. **Deploy 2 S3 buckets**: One to host the static website and another to store CodePipeline artifacts.
2. **Deploy CodePipeline**: Configure the pipeline to access the GitHub repository, retrieve the necessary files, and store the intermediate artifacts in the artifacts bucket.
3. **Final Deployment**: CodePipeline deploys the final website files (e.g., HTML, CSS, JavaScript) to the designated bucket, making them publicly accessible as a static website.
4. **Automation**: Set up a GitHub workflow to sync with the static website whenever a change is committed to the repository.

### Difficulties

As this was my first time using GitHub as the source for a static website, it took me a while to adjust the necessary permissions to allow the pipeline to interact with GitHub. Additionally, I had to read many GitHub documentation pages to fully understand how to use GitHub Actions to sync the bucket with GitHub.

## Using Terraform

**URL:** [http://terrabucketauto.s3-website-ap-southeast-2.amazonaws.com/](http://terrabucketauto.s3-website-ap-southeast-2.amazonaws.com/)

Next, I experimented with Terraform to improve my skill set. Despite CloudFormation being useful, Terraform could interact with other cloud services easily. Moreover, Terraform seemed simpler to use and handle, with its syntax being much more straightforward and intuitive. I used AWS cloud to set up my S3 bucket using Terraform.

### Logic

Here is the logic behind my Terraform template:

1. **Deploy S3 Bucket**: Terraform deploys an S3 bucket with an empty `index.html` and `error.html` file.
2. **GitHub Actions**: Using a similar GitHub action as before, I commit a change which syncs the empty bucket with the GitHub repository, creating a static website that will continue to sync with any changes.

### Difficulties

During the deployment process, there were issues with the `.git` directory being included in the upload to S3. This was resolved by excluding the `.git` directory in the `aws s3 sync` command in the GitHub Actions workflow. Additionally, there were issues with configuring public access for the S3 bucket. Initially, the `acl` attribute caused errors due to the bucket's object ownership settings. This was resolved by configuring the bucket policy to allow public read access instead of using ACLs.

## Using Ansible

Lastly, I tried out Ansible, a powerful configuration management tool that works on multiple cloud platforms.

### Logic

Here is the logic:
1. **Deploy EC2 Instance**: An EC2 instance is deployed to host the website.
2. **Configure EC2 with Ansible**: Using Ansible, I configured the instance to install Apache (to act as a web server) and Git (to retrieve files from GitHub).
3. **Clone GitHub Repository**: The EC2 instance clones the GitHub repository to set up a static website as needed.

### Conclusion

Using multiple tools like CloudFormation, Terraform, and Ansible allowed me to explore different methods of deploying and managing infrastructure. Each tool has its strengths, and I gained valuable insights by working with all three.

#### Note
The files `deploy.yml` and `Deploy to S3.yml` are the Github workflow files that gives github action the instructions. I had also cloned the html template given, and sync my websites to my own cloned repository. This allowed me to test whether commits to the repository resulted in updates in the websites.
