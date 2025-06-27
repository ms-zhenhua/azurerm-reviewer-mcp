import unittest
from reviewer import generate_file_chunks

file_content = """\
// Copyright (c) HashiCorp, Inc.
// SPDX-License-Identifier: MPL-2.0

package applicationinsights

import (
	"context"
	"encoding/base64"
	"fmt"
	"strings"
	"time"

	"github.com/hashicorp/go-azure-helpers/lang/pointer"
	"github.com/hashicorp/go-azure-helpers/lang/response"
	"github.com/hashicorp/go-azure-helpers/resourcemanager/commonschema"
	"github.com/hashicorp/go-azure-helpers/resourcemanager/location"
	components "github.com/hashicorp/go-azure-sdk/resource-manager/applicationinsights/2020-02-02/componentsapis"
	webtests "github.com/hashicorp/go-azure-sdk/resource-manager/applicationinsights/2022-06-15/webtestsapis"
	"github.com/hashicorp/terraform-provider-azurerm/internal/sdk"
	"github.com/hashicorp/terraform-provider-azurerm/internal/tf/pluginsdk"
	"github.com/hashicorp/terraform-provider-azurerm/internal/tf/validation"
	"github.com/hashicorp/terraform-provider-azurerm/utils"
)

var (
	_ sdk.ResourceWithUpdate        = ApplicationInsightsStandardWebTestNewResource{}
	_ sdk.ResourceWithCustomizeDiff = ApplicationInsightsStandardWebTestNewResource{}
)

type ApplicationInsightsStandardWebTestNewResource struct{}

type ApplicationInsightsStandardWebTestNewResourceModel struct {
	Name                  string                `tfschema:"name"`
	ResourceGroupName     string                `tfschema:"resource_group_name"`
	ApplicationInsightsID string                `tfschema:"application_insights_id"`
	Location              string                `tfschema:"location"`
	Frequency             int64                 `tfschema:"frequency"`
	Timeout               int64                 `tfschema:"timeout"`
	Enabled               bool                  `tfschema:"enabled"`
	Retry                 bool                  `tfschema:"retry_enabled"`
	Request               []RequestModel        `tfschema:"request"`
	ValidationRules       []ValidationRuleModel `tfschema:"validation_rules"`
	GeoLocations          []string              `tfschema:"geo_locations"`
	Description           string                `tfschema:"description"`
	Tags                  map[string]interface{}     `tfschema:"tags"`

	// ComputedOnly
	SyntheticMonitorID string `tfschema:"synthetic_monitor_id"`
}

type RequestModel struct {
	FollowRedirects        bool          `tfschema:"follow_redirects_enabled"`
	HTTPVerb               string        `tfschema:"http_verb"`
	ParseDependentRequests bool          `tfschema:"parse_dependent_requests_enabled"`
	Header                 []HeaderModel `tfschema:"header"`
	Body                   string        `tfschema:"body"`
	URL                    string        `tfschema:"url"`
}

type ValidationRuleModel struct {
	ExpectedStatusCode           int64          `tfschema:"expected_status_code"`
	CertificateRemainingLifetime int64          `tfschema:"ssl_cert_remaining_lifetime"`
	SSLCheck                     bool           `tfschema:"ssl_check_enabled"`
	Content                      []ContentModel `tfschema:"content"`
}

type HeaderModel struct {
	Name  string `tfschema:"name"`
	Value string `tfschema:"value"`
}

type ContentModel struct {
	ContentMatch    string `tfschema:"content_match"`
	IgnoreCase      bool   `tfschema:"ignore_case"`
	PassIfTextFound bool   `tfschema:"pass_if_text_found"`
}

func (r ApplicationInsightsStandardWebTestNewResource) CustomizeDiff() sdk.ResourceFunc {
	return sdk.ResourceFunc{
		Timeout: 5 * time.Minute,
		Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
			rd := metadata.ResourceDiff

			// SSLCheck conditions
			url, ok := rd.GetOk("request.0.url")
			if ok {
				if !strings.HasPrefix(strings.ToLower(url.(string)), "https://") {
					if v, ok := rd.GetOkExists("validation_rules.0.ssl_check_enabled"); ok && v.(bool) {
						return fmt.Errorf("cannot set ssl_check_enabled to true if request.0.url is not https")
					}
					if v, ok := rd.GetOkExists("validation_rules.0.ssl_cert_remaining_lifetime"); ok && v.(int) != 0 {
						return fmt.Errorf("cannot set ssl_cert_remaining_lifetime if request.0.url is not https")
					}
				}
			}

			return nil
		},
	}
}"""

class TestStringMethods(unittest.TestCase):
    def test_generate_file_chunks(self):
        chunks = generate_file_chunks(file_content, max_chunk_size=1000)
        file_content_lines = []

        next_line_no = 1
        for chunk in chunks:
            lines = chunk.splitlines()
            for line in lines:
                no, content = line.split(' ', 1)
                if int(no.strip()) != next_line_no:
                    continue

                file_content_lines.append(content)
                next_line_no += 1

        self.assertEqual(file_content, "\n".join(file_content_lines))
        

if __name__ == '__main__':
    unittest.main()