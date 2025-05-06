# -*- coding: utf-8 -*-

"""
IAM policy statement constructors.

Provides factory functions and helper classes to create AWS IAM policy statements
with correct structure and syntax. Simplifies the creation of common permission
patterns while ensuring policy best practices.
"""

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam

from func_args.api import T_OPT_KWARGS


prefix = "Cdkit"


def create_get_caller_identity_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allows the caller to get their identity.
    """
    if policy_statement_kwargs is None:  # pragma: no cover
        policy_statement_kwargs = {
            "sid": f"{prefix}AllowGetCallerIdentity",
        }
    return iam.PolicyStatement(
        actions=["sts:GetCallerIdentity"],
        resources=["*"],
        **policy_statement_kwargs,
    )


def create_assume_role_statement(
    role_to_assume_arn_list: list[str],
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allows assuming specific roles.

    :param role_to_assume_arn_list: List of ARNs of roles to assume.
    """
    if policy_statement_kwargs is None:  # pragma: no cover
        policy_statement_kwargs = {
            "sid": f"{prefix}AllowAssumeOtherRoles",
        }
    return iam.PolicyStatement(
        actions=["sts:AssumeRole"],
        resources=role_to_assume_arn_list,
        **policy_statement_kwargs,
    )


def create_allow_all_services_except_identity_management_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allow access to all AWS services except identity management services
    (IAM, Organizations, Account).

    The principal is denied actions related to IAM, Organizations,
    and Account, but allowed all other actions.
    """
    if policy_statement_kwargs is None:
        policy_statement_kwargs = {
            "sid": f"{prefix}AllowAllServicesExceptIdentityManagement",
        }
    return iam.PolicyStatement(
        not_actions=[
            "account:*",
            "organizations:*",
            "iam:*",
        ],
        resources=["*"],
        **policy_statement_kwargs,
    )


def create_account_and_org_and_iam_read_only_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allow read-only access to IAM, Organizations, and Account resources.

    The principal can view configuration details of these resources,
    but cannot modify or create them.
    """
    if policy_statement_kwargs is None:  # pra
        policy_statement_kwargs = {
            "sid": f"{prefix}AllowAccountAndOrgAndIamReadOnly",
        }
    return iam.PolicyStatement(
        actions=[
            "account:GetAccountInformation",
            "account:GetPrimaryEmail",
            "account:ListRegions",
            "iam:GetAccountName",
            "iam:GetAccountSummary",
            "iam:GetContextKeysForCustomPolicy",
            "iam:GetInstanceProfile",
            "iam:GetPolicy",
            "iam:GetPolicyVersion",
            "iam:GetRole",
            "iam:GetRolePolicy",
            "iam:ListAccountAliases",
            "iam:ListAttachedGroupPolicies",
            "iam:ListAttachedRolePolicies",
            "iam:ListCloudFrontPublicKeys",
            "iam:ListEntitiesForPolicy",
            "iam:ListGroupPolicies",
            "iam:ListGroups",
            "iam:ListGroupsForUser",
            "iam:ListInstanceProfileTags",
            "iam:ListInstanceProfiles",
            "iam:ListInstanceProfilesForRole",
            "iam:ListOpenIDConnectProviderTags",
            "iam:ListOpenIDConnectProviders",
            "iam:ListPolicies",
            "iam:ListPoliciesGrantingServiceAccess",
            "iam:ListPolicyTags",
            "iam:ListPolicyVersions",
            "iam:ListRolePolicies",
            "iam:ListRoleTags",
            "iam:ListRoles",
            "iam:ListSTSRegionalEndpointsStatus",
            "iam:ListServerCertificateTags",
            "iam:ListServerCertificates",
            "iam:ListServiceSpecificCredentials",
            "organizations:DescribeOrganization",
        ],
        resources=["*"],
        **policy_statement_kwargs,
    )


def create_prefixed_iam_management_statement(
    prefix: str,
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allow full IAM management access for resources prefixed with the given string.

    The principal can manage IAM instance profiles, policies, and roles
    whose names start with the specified prefix.
    """
    if policy_statement_kwargs is None:
        policy_statement_kwargs = {
            "sid": f"{prefix}AllowPrefixedIamManagement",
        }
    return iam.PolicyStatement(
        actions=[
            "iam:AddRoleToInstanceProfile",
            "iam:AttachRolePolicy",
            "iam:CreateInstanceProfile",
            "iam:CreatePolicy",
            "iam:CreatePolicyVersion",
            "iam:CreateServiceLinkedRole",
            "iam:DeleteInstanceProfile",
            "iam:DeletePolicy",
            "iam:DeletePolicyVersion",
            "iam:DeleteRole",
            "iam:DeleteRolePolicy",
            "iam:DetachRolePolicy",
            "iam:PassRole",
            "iam:PutRolePolicy",
            "iam:SimulateCustomPolicy",
            "iam:SimulatePrincipalPolicy",
            "iam:TagInstanceProfile",
            "iam:TagPolicy",
            "iam:TagRole",
            "iam:UntagInstanceProfile",
            "iam:UntagPolicy",
            "iam:UntagRole",
            "iam:UpdateAssumeRolePolicy",
            "iam:UpdateRoleDescription",
        ],
        resources=[
            f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:instance-profile/{prefix}*",
            f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:policy/{prefix}*",
            f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:role/{prefix}*",
        ],
        **policy_statement_kwargs,
    )


def create_require_permission_boundary_for_role_creation_statement(
    policy_name: str,
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allow creation of IAM roles only if a specific permissions boundary is attached.

    The principal can create roles only when the specified permissions boundary policy is applied.
    """
    if policy_statement_kwargs is None:
        policy_statement_kwargs = {
            "sid": f"{prefix}RequirePermissionBoundaryForRoleCreation",
        }
    return iam.PolicyStatement(
        sid="RequirePermissionBoundaryForRoleCreation",
        actions=[
            "iam:CreateRole",
        ],
        resources=[
            f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:role/*",
        ],
        conditions={
            "StringEquals": {
                "iam:PermissionsBoundary": f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:policy/{policy_name}"
            }
        },
        **policy_statement_kwargs,
    )


def create_restricted_read_only_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Grant read-only access across a wide range of AWS services,
    excluding any write or management actions.
    """
    if policy_statement_kwargs is None:
        policy_statement_kwargs = {
            "sid": f"{prefix}RestrictedReadOnly",
        }
    return iam.PolicyStatement(
        actions=[
            "apigateway:GET",
            "appsync:Get*",
            "appsync:List*",
            "athena:Batch*",
            "athena:Get*",
            "athena:List*",
            "batch:Describe*",
            "batch:List*",
            "cloud9:Describe*",
            "cloud9:List*",
            "cloudformation:Describe*",
            "cloudformation:Detect*",
            "cloudformation:Estimate*",
            "cloudformation:Get*",
            "cloudformation:List*",
            "cloudtrail:Describe*",
            "cloudtrail:Get*",
            "cloudtrail:List*",
            "cloudwatch:Describe*",
            "cloudwatch:Get*",
            "cloudwatch:List*",
            "codeartifact:DescribeDomain",
            "codeartifact:DescribePackage",
            "codeartifact:DescribePackageVersion",
            "codeartifact:DescribeRepository",
            "codeartifact:GetDomainPermissionsPolicy",
            "codeartifact:GetPackageVersionAsset",
            "codeartifact:GetPackageVersionReadme",
            "codeartifact:GetRepositoryEndpoint",
            "codeartifact:GetRepositoryPermissionsPolicy",
            "codeartifact:List*",
            "codebuild:BatchGet*",
            "codebuild:DescribeCodeCoverages",
            "codebuild:DescribeTestCases",
            "codebuild:List*",
            "codecommit:BatchGet*",
            "codecommit:Describe*",
            "codecommit:Get*",
            "codecommit:List*",
            "codedeploy:BatchGet*",
            "codedeploy:Get*",
            "codedeploy:List*",
            "dynamodb:DescribeBackup",
            "dynamodb:DescribeContinuousBackups",
            "dynamodb:DescribeContributorInsights",
            "dynamodb:DescribeEndpoints",
            "dynamodb:DescribeExport",
            "dynamodb:DescribeGlobalTable",
            "dynamodb:DescribeGlobalTableSettings",
            "dynamodb:DescribeImport",
            "dynamodb:DescribeKinesisStreamingDestination",
            "dynamodb:DescribeLimits",
            "dynamodb:DescribeReservedCapacity",
            "dynamodb:DescribeReservedCapacityOfferings",
            "dynamodb:DescribeStream",
            "dynamodb:DescribeTable",
            "dynamodb:DescribeTableReplicaAutoScaling",
            "dynamodb:DescribeTimeToLive",
            "dynamodb:GetResourcePolicy",
            "dynamodb:List*",
            "ec2:Describe*",
            "ec2:Get*",
            "ecr:Get*",
            "ecr:List*",
            "ecs:Describe*",
            "ecs:List*",
            "eks:Describe*",
            "eks:List*",
            "elasticfilesystem:Describe*",
            "elasticfilesystem:List*",
            "elasticloadbalancing:Describe*",
            "events:Describe*",
            "events:List*",
            "firehose:Describe*",
            "firehose:List*",
            "glue:BatchGet*",
            "glue:Get*",
            "glue:List*",
            "iam:Get*",
            "iam:List*",
            "kinesis:Describe*",
            "kinesis:Get*",
            "kinesis:List*",
            "kinesisanalytics:Describe*",
            "kinesisanalytics:Get*",
            "kinesisanalytics:List*",
            "kinesisvideo:Describe*",
            "kinesisvideo:Get*",
            "kinesisvideo:List*",
            "kms:Describe*",
            "kms:Describe*",
            "lakeformation:Describe*",
            "lakeformation:Get*",
            "lakeformation:Search*",
            "lakeformation:List*",
            "lambda:Get*",
            "lambda:List*",
            "logs:Describe*",
            "logs:List*",
            "rds:Describe*",
            "rds:Download*",
            "rds:List*",
            "redshift-serverless:Get*",
            "redshift-serverless:List*",
            "redshift:Describe*",
            "route53:Get*",
            "s3:GetBucketAcl",
            "s3:GetBucketCORS",
            "s3:GetBucketLocation",
            "s3:GetBucketLogging",
            "s3:GetBucketNotification",
            "s3:GetBucketObjectLockConfiguration",
            "s3:GetBucketOwnershipControls",
            "s3:GetBucketPolicy",
            "s3:GetBucketPolicyStatus",
            "s3:GetBucketPublicAccessBlock",
            "s3:GetBucketRequestPayment",
            "s3:GetBucketTagging",
            "s3:GetBucketVersioning",
            "s3:GetBucketWebsite",
            "s3:List*",
            "sagemaker:Describe*",
            "sagemaker:Get*",
            "sagemaker:List*",
            "secretsmanager:Describe*",
            "secretsmanager:List*",
            "ses:BatchGetMetricData",
            "ses:Describe*",
            "ses:Get*",
            "ses:List*",
            "sns:Get*",
            "sns:List*",
            "sqs:Get*",
            "sqs:List*",
            "ssm:Describe*",
            "ssm:Get*",
            "ssm:List*",
            "sts:Get*",
        ],
        resources=["*"],
        **policy_statement_kwargs,
    )
