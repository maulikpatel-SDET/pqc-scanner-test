# TLS keys, certificates and legacy TLS policies. TEST ONLY.

resource "tls_private_key" "server" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "tls_private_key" "ecdsa" {
  algorithm   = "ECDSA"
  ecdsa_curve = "P256"
}

resource "tls_self_signed_cert" "server" {
  private_key_pem = tls_private_key.server.private_key_pem
  subject { common_name = "testbed.local" }
  validity_period_hours = 87600
  allowed_uses          = ["server_auth"]
}

resource "aws_lb_listener" "https" {
  load_balancer_arn = var.lb_arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS-1-0-2015-04"
  certificate_arn   = var.cert_arn
  default_action {
    type             = "forward"
    target_group_arn = var.tg_arn
  }
}

resource "aws_cloudfront_distribution" "cdn" {
  enabled = true
  viewer_certificate {
    acm_certificate_arn      = var.cert_arn
    minimum_protocol_version = "TLSv1"
    ssl_support_method       = "sni-only"
  }
}

resource "aws_acm_certificate" "cert" {
  domain_name       = "testbed.local"
  validation_method = "DNS"
  key_algorithm     = "RSA_2048"
}

resource "azurerm_storage_account" "sa" {
  name                     = "testbedsa"
  resource_group_name      = var.rg
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_0"
}
